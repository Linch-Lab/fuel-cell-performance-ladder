# Fuel Cell Performance Ladder

> 燃料電池性能天梯——各類型燃料電池技術的峰值功率密度與電流密度世界紀錄資料庫（2016–2026）

![License: MIT (Code)](https://img.shields.io/badge/License-MIT-blue.svg)
![Data: CC BY 4.0](https://img.shields.io/badge/Data-CC%20BY%204.0-lightgrey.svg)

## 關於本專案

本專案提供**各類型燃料電池技術**的峰值功率密度 (W/cm²) 與特定電壓下電流密度 (A/cm² @ 0.65 V) 之最佳紀錄資料庫，時間範圍 2016–2026。靈感來自 NREL 的 [Best Research-Cell Efficiency Chart](https://www.nrel.gov/pv/cell-efficiency.html)。

每筆資料經 **三源驗證**：
1. ✅ **MinerU 解析**論文 PDF 原文（[mineru-paper-reading](https://github.com/Linch-Lab/academic-skill)）
2. ✅ **讀圖取點**：從論文極化曲線圖讀取數據點（[plot-data-extraction](../../../AppData/Local/hermes/skills/data-science/plot-data-extraction))
3. ✅ **DOI/來源核對**：Crossref/OpenAlex 驗證

## 技術類型

| 代號 | 技術 | 操作條件 |
|------|------|----------|
| PEMFC | 質子交換膜燃料電池（低溫） | 60–80°C, H₂/Air 或 H₂/O₂ |
| HT-PEMFC | 高溫 PBI 質子交換膜 | 140–200°C, H₂/Air |
| O-SOFC | 陽極支撐固態氧化物燃料電池 | 650–800°C, H₂/Air |
| P-SOFC | 電解質支撐固態氧化物燃料電池 | 700–900°C, H₂/Air |
| AEMFC | 陰離子交換膜燃料電池 | 60–90°C, H₂/O₂ 或 H₂/Air |
| 商用系統 | 車用電堆等（另列） | 見資料表 |

## 目錄結構

```
fuel-cell-performance-ladder/
├── data/                    # 資料 CSV（三源驗證後）
│   ├── fc_peak_power.csv    # 峰值功率密度 × 年份
│   └── fc_current_density.csv # 電流密度@0.65V × 年份
├── figures/                 # 產出圖（PNG）
├── src/                     # 生成腳本
│   ├── generate_chart.py    # 上下雙子圖生成
│   └── extract_points.py    # 讀圖取點（plot-data-extraction 調用）
├── references/              # 原始文獻（PDF + MinerU 輸出）
├── docs/                    # 資料方法學、更新指南
├── index.html               # 互動圖表（GitHub Pages 部署）
├── LICENSE                  # MIT（程式碼）
├── DATA_LICENSE             # CC BY 4.0（資料與圖）
└── README.md
```

## 使用方法

### 資料
`data/*.csv` 為機器可讀的資料庫，欄位：
```
year, technology, metric, value, unit, operating_conditions, source_doi, verification_level, notes
```

### 圖表
- `figures/*.png`：靜態圖（上：峰值功率密度；下：電流密度@0.65V）
- `index.html`：互動圖（hover 顯示操作條件與來源）

### 複現
```bash
pip install -r requirements.txt
python src/generate_chart.py
```

## 資料方法學

見 [docs/methodology.md](docs/methodology.md)

## 引用

若使用本資料庫，請引用：
```
Li, C.-H. (2026). Fuel Cell Performance Ladder. Zenodo/GitHub.
https://github.com/Linch-Lab/fuel-cell-performance-ladder
```

## 授權

- **程式碼**：MIT License
- **資料與圖**：CC BY 4.0（需署名）

## 貢獻

本專案為靜態交付——需要更新時請開 Issue 或 PR（附 DOI 與操作條件）。
