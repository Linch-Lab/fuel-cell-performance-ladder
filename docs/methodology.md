# 資料方法學

## 三源驗證流程

每筆資料點必須通過以下三步驟：

### 1. MinerU 解析 PDF
使用 [mineru-paper-reading](https://github.com/Linch-Lab/academic-skill) skill 解析論文 PDF：
- 輸出結構化 Markdown（含表格、公式、圖片）
- 定位極化曲線圖與性能數據表

### 2. 讀圖取點
使用 [plot-data-extraction](../../../AppData/Local/hermes/skills/data-science/plot-data-extraction) skill 從極化曲線圖讀取數據：
- **tick 線校準**（非標籤文字中心）
- **hue 分色**分離多條曲線
- **腐蝕法**隔離 marker 符號（質心 = 數據點）
- 重疊曲線規則：被蓋曲線取頂層曲線值
- 輸出 (V, I) 點後，取 0.65V 交點與峰值功率

### 3. DOI/來源核對
- Crossref / OpenAlex API 驗證 DOI 存在
- 記錄操作條件（溫度、壓力、氣體、膜材料）
- 標註驗證等級

## 驗證等級

| 等級 | 說明 |
|------|------|
| 🔴 直接引用 | 論文原文直接給數值（表格/文字）|
| 🟡 讀圖取點 | 從極化曲線圖讀取（含讀圖誤差 ±5-10%）|
| 🟢 二級來源 | 彙整報告（IEA/DOE 等）|

## 數據欄位

```
year: 紀錄發表年份
technology: 技術代號（見 README）
metric: 指標（peak_power_density / current_density@0.65V）
value: 數值
unit: 單位
operating_conditions: 操作條件（溫度/壓力/氣體/膜）
source_doi: DOI
verification_level: 🔴/🟡/🟢
notes: 備註（含讀圖誤差說明）
```

## 同年多筆紀錄

同年取最高值（NREL「best research cell」精神），其他紀錄保留於 notes 或 secondary CSV。
