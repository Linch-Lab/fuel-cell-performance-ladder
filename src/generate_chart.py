#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Fuel Cell Performance Ladder — 上下雙子圖生成
上：峰值功率密度 (W/cm²) × 年份
下：電流密度 @0.65V (A/cm²) × 年份
2016–2026，每技術一條線，同年取最高值

用法: python src/generate_chart.py
輸出: figures/fc_performance_ladder.png (+ 互動 HTML index.html)
"""
import csv
import json
import os
import sys
from collections import defaultdict

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(REPO, 'data')
FIG_DIR = os.path.join(REPO, 'figures')
HTML_OUT = os.path.join(REPO, 'index.html')

# 技術顏色（NREL 風格）
TECH_COLORS = {
    'PEMFC': '#e6194b',
    'HT-PEMFC': '#3cb44b',
    'O-SOFC': '#4363d8',
    'P-SOFC': '#f58231',
    'AEMFC': '#911eb4',
    'COMMERCIAL': '#808080',
}
TECH_LABELS = {
    'PEMFC': 'PEMFC (LT)',
    'HT-PEMFC': 'HT-PEMFC (PBI)',
    'O-SOFC': 'O-SOFC (anode-supported)',
    'P-SOFC': 'P-SOFC (electrolyte-supported)',
    'AEMFC': 'AEMFC',
    'COMMERCIAL': 'Commercial systems',
}


# 催化劑類型 marker 形狀（嚴格二分：PGM vs PGM-free）
CATALYST_MARKERS = {
    'PGM': 'o',          # 貴金屬（含純 Pt 與 Pt 合金）
    'PGM-free': 's',     # 全非貴金屬
}


def load_csv(metric):
    """載入 data/fc_*.csv，回傳 {tech: [(year, cat, value), ...]} 同年同類取最高"""
    fname = 'fc_peak_power.csv' if metric == 'peak_power' else 'fc_current_density.csv'
    path = os.path.join(DATA_DIR, fname)
    if not os.path.exists(path):
        print(f"⚠️ 缺少 {path} — 建立空資料")
        return {}
    by_tech = defaultdict(dict)
    with open(path, encoding='utf-8-sig') as fh:
        for r in csv.DictReader(fh):
            tech = r['technology']
            cat = r.get('catalyst_type', 'PGM')
            year = int(r['year'])
            val = float(r['value'])
            key = (year, cat)
            # 同年同催化劑類取最高
            if key not in by_tech[tech] or val > by_tech[tech][key][1]:
                by_tech[tech][key] = (val, cat)
    # 轉成 [(year, cat, value), ...] 排序
    return {t: sorted([(y, c, v) for (y, c), (v, _) in d.items()])
            for t, d in by_tech.items()}


def draw_subplot(ax, data, ylabel, title):
    for tech, pts in data.items():
        if not pts:
            continue
        years = [p[0] for p in pts]
        vals = [p[2] for p in pts]
        cats = [p[1] for p in pts]
        color = TECH_COLORS.get(tech, '#000000')
        label = TECH_LABELS.get(tech, tech)
        # 同技術連線（虛線），點用催化劑形狀
        ax.plot(years, vals, '-', color=color, linewidth=1.2, alpha=0.7)
        for y, v, c in pts:
            m = CATALYST_MARKERS.get(c, 'o')
            ax.plot(y, v, m, color=color, markersize=8,
                    label=label if (tech, c) not in ax._legend_labels else None)
            ax._legend_labels.add((tech, c))
        ax.set_xlim(2015.5, 2026.5)
        ax.set_xticks(range(2016, 2027, 2))
        ax.set_ylabel(ylabel, fontsize=11)
        ax.set_title(title, fontsize=12)
        ax.grid(True, alpha=0.3)
        if not hasattr(ax, '_legend_added'):
            ax.legend(loc='upper left', fontsize=8, framealpha=0.8)
            ax._legend_added = True
    ax.legend(loc='upper left', fontsize=8, framealpha=0.8)


def main():
    os.makedirs(FIG_DIR, exist_ok=True)

    peak = load_csv('peak_power')
    curr = load_csv('current_density')

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 10), sharex=False)
    draw_subplot(ax1, peak, 'Peak power density (W/cm²)',
                 'Fuel Cell Performance Ladder — Peak Power Density (2016–2026)')
    draw_subplot(ax2, curr, 'Current density @0.65V (A/cm²)',
                 'Current Density at 0.65 V (2016–2026)')
    ax2.set_xlabel('Year', fontsize=11)

    plt.tight_layout()
    png_path = os.path.join(FIG_DIR, 'fc_performance_ladder.png')
    plt.savefig(png_path, dpi=200, bbox_inches='tight')
    print(f"✅ PNG: {png_path}")

    # 互動 HTML（內嵌數據 JSON）
    data_json = json.dumps({
        'peak_power': {t: [{'year': y, 'value': v} for y, v in pts]
                       for t, pts in peak.items()},
        'current_density': {t: [{'year': y, 'value': v} for y, v in pts]
                            for t, pts in curr.items()},
    }, ensure_ascii=False)
    colors_json = json.dumps(TECH_COLORS, ensure_ascii=False)

    html_template = """<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<title>Fuel Cell Performance Ladder</title>
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<style>body{{font-family: sans-serif; margin: 2rem;}}
table{{border-collapse: collapse; margin-top: 1rem;}}
th,td{{border: 1px solid #ccc; padding: 4px 10px; font-size: 12px;}}</style>
</head>
<body>
<h1>Fuel Cell Performance Ladder</h1>
<p>各類型燃料電池最佳性能紀錄（2016–2026）。資料經三源驗證（MinerU 解析 + 讀圖取點 + DOI 核對）。</p>
<div id="chart"></div>
<h2>操作條件參考資料</h2>
<div id="refs"></div>
<script>
const DATA = __DATA__;
const colors = __COLORS__;
const techs = Object.keys(colors);
const METRICS = ['peak_power', 'current_density'];
const TITLES = ['Peak Power Density (W/cm²)', 'Current Density @0.65V (A/cm²)'];
const trAll = [];
for (let mi = 0; mi < METRICS.length; mi++) {{
    const metric = METRICS[mi];
    for (const tech of techs) {{
        const pts = (DATA[metric] || {{}})[tech] || [];
        trAll.push({{
            x: pts.map(p => p.year),
            y: pts.map(p => p.value),
            mode: 'lines+markers',
            name: tech + (mi === 1 ? ' (I@0.65V)' : ''),
            line: {{color: colors[tech] || '#000', width: 2}},
            marker: {{size: 7, color: colors[tech] || '#000'}},
            xaxis: 'x' + (mi + 1),
            yaxis: 'y' + (mi + 1),
        }});
    }}
}}
const layout = {{
    grid: {{rows: 2, columns: 1, pattern: 'independent'}},
    title: 'Fuel Cell Performance Ladder (2016–2026)',
    showlegend: true,
    height: 900,
    xaxis: {{title: 'Year', range: [2015.5, 2026.5], dtick: 2}},
    xaxis2: {{title: 'Year', range: [2015.5, 2026.5], dtick: 2}},
    yaxis: {{title: TITLES[0]}},
    yaxis2: {{title: TITLES[1]}},
}};
Plotly.newPlot('chart', trAll, layout);
</script>
</body>
</html>"""
    html = html_template.replace('__DATA__', data_json).replace('__COLORS__', colors_json)
    with open(HTML_OUT, 'w', encoding='utf-8') as fh:
        fh.write(html)
    print(f"✅ HTML: {HTML_OUT}")


if __name__ == '__main__':
    main()
