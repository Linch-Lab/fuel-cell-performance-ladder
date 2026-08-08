# FC Review 閱讀筆記

> 燃料電池性能天梯（fuel-cell-performance-ladder）文獻閱讀彙整
> 更新：2026-08-09

---

## R2. PEMFC 催化劑 Review (2025 IJHE) ✅ 已讀

**文獻**：(2025). "Evaluating electrocatalytic activities of Pt, Pd, Au and Ag-based catalyst on PEMFC performance: A review." *Int. J. Hydrogen Energy*
**狀態**：✅ MinerU 解析 + 深讀完成（796 行）

### PEMFC 催化劑性能數據點

| 催化劑 | 質量活性 (A/mg) | 功率密度 (mW/cm²) | 類別 | 備註 |
|------|:--:|:--:|:--:|------|
| ZIF-derived Pt-Co-Ni 三元合金 | 1.36 (9.87×Pt/C) | **2031** | PGM | 最高紀錄 |
| Au(core)@Pt(shell) | — | **>2000** | PGM | >10,000 cycles 穩定 |
| Pt-Pd 奈米樹枝狀 | 0.27 (3×Pt) | **1365** | PGM | |
| Pt-Pd/C 耦合 | — | 1300 | PGM | |
| PtCo（impregnation 優化）| 1.08 @0.9V | 1170 | PGM | H₂-air |
| PtFeCo/C | — | 841 | PGM | |
| De-alloyed PtCu/C | — | 672 | PGM | |
| Pd-Au/FGP | — | 414 | PGM (Pd-based) | |

### 關鍵結論
- PEMFC 主流仍是 Pt/Pd 基（PGM）；PtCo/PtNi 合金質量活性更高
- Ag 低成本替代：Ag/Pt 混合 +30% 功率密度
- Au@Pt 核殼 >2 W/cm² 且 10,000 cycles 無衰減（2020s 里程碑）
- 陰極 Pt 佔全電池 80-90%（ORR 慢 5 數量級）

---

## R1. HT-PEMFC Review (2021 Chem Soc Rev) ✅ 已讀

**文獻**：Wang et al. (2021). "High temperature proton exchange membrane fuel cells: progress in advanced materials and key technologies." *Chem. Soc. Rev.* DOI: 10.1039/d0cs00296h
**狀態**：✅ MinerU 解析 + 深讀完成（1526 行）

### HT-PEMFC 性能數據點

| 年份 | 峰值功率 (mW/cm²) | 操作條件 | 催化劑 | 來源 |
|:--:|:--:|:--:|:--:|:--:|
| 2016 | 512 | 120°C, CNT/ABPBI/Pt@IL | Pt 0.3 mg/cm² | Luo et al. |
| 2016 | 482 (H₂/O₂) / 321 (H₂/air) | 160°C, 常壓 | Pt 0.1 mg/cm², binderless | — |
| 2016 | 320 | 150°C, 20wt% Pt/C | Pt 0.2 mg/cm², MPL-free | — |
| 2018 | 184.6 | 160°C, H₂/O₂ 常壓 | **Fe–N–C（PGM-free）** | Hu et al. |
| — | 715 | 150°C, 膜固定化 | Pt | — |
| — | 269.9 | 160°C, O₂, 100h | Pt/C | Lobato et al. |

### 關鍵結論
- HT-PEMFC 主流 = Pt 基；PGM-free（Fe–N–C）在 HT 剛起步（2018 僅 184.6 mW/cm²）
- Pa/PBI 膜磷酸毒化是 PGM-free 在 HT 的主要障礙
- 操作條件：120–180°C、常壓、H₂/O₂ 或 H₂/air
- HT 電堆成本 $840/kW（低產量）比 LT 高 47%

---

## R5. AEMFC Review (2018 JPS) ✅ 已讀

**文獻**：Dekel, D. R. (2018). "Review of cell performance in anion exchange membrane fuel cells." *J. Power Sources* 375, 158-169. DOI: 10.1016/j.jpowsour.2017.07.117
**狀態**：✅ MinerU 解析 + 深讀完成

### 核心數據（H₂-fueled AEMFC）

| 時期 | 0.8V 電流 | 極限電流 | 峰值功率 |
|------|:--:|:--:|:--:|
| ≤2007 | 40–70 mA/cm² | 60–220 mA/cm² | 20–120 mW/cm² |
| 2016–2017 | 450–620 mA/cm² | >2500 mA/cm² | **>1000 mW/cm² (1 W/cm²)** |

- 0.6V 電流：800–2300 mA/cm²（2014-2017 最佳）
- 操作：60–80°C、純 O₂（多數）、CO₂-free/filtered air

### 催化劑分類（PGM/PGM-free 二分依據）

| 類別 | ORR | HOR | 性能 |
|------|:--:|:--:|:--:|
| PGM | Pt | PtRu（活性 2-6×Pt）| **>1 W/cm²** |
| PGM-free | 非貴金屬 | 非貴金屬 | <100 mW/cm² |
| Pd-based | — | Pd-Ni / Pd-CeO₂ | 100-300 mW/cm² |

- 高性能 AEMFC 全用 Pt/PtRu；完全 PGM-free 僅 ~5 篇、<100 mW/cm²
- **Fig 5a：峰值功率密度 × 年份彙整（2000-2017）→ 可讀圖取點**

### 天梯數據點（AEMFC, PGM）

| 年份 | 峰值功率 (mW/cm²) | 操作條件 | 來源 |
|:--:|:--:|:--:|:--:|
| 2006 | ~20 | 純 O₂ | Fig 5a 讀圖（待取）|
| 2010 | ~100 | 純 O₂ | Fig 5a 讀圖（待取）|
| 2015 | ~400 | 純 O₂ | Fig 5a 讀圖（待取）|
| 2016 | ~700 | 純 O₂ | Fig 5a 讀圖（待取）|
| 2017 | **>1000** | 60-80°C, O₂, PtRu | Fig 5a/6 讀圖（待取）|

> ⚠️ 數值待從 Fig 5a 讀圖精確取點（plot-data-extraction）

### 其他
- 直接液體燃料：甲醇 130 / 乙醇 180 / 聯氨 450 mW/cm²
- 耐久：多數 <300h、衰減 0.2–0.5 mV/h（比 PEMFC 高 2 數量級）

---

## R3. PEMFC lower-cost (2021 APLM Scilight) ✅ 已讀（摘要）

**文獻**：Meeri Kim (2021). "Progress towards lower-cost PEM fuel cells." *Scilight* 2021, 141110. DOI: 10.1063/10.0004268
**狀態**：✅ MinerU 解析（此篇為 Scilight 新聞，非完整 review）

### 要點
- 完整 review 為：**Mølmen et al., APL Mater. 2021, DOI: 10.1063/5.0045801**（需補下載）
- 催化劑分類：**PGM-based vs PGM-free**（支持嚴格二分）
  - PGM-based：Pt-合金（Fe/Co/Ni/Cu）、空心奈米粒子、碳基質包覆
  - PGM-free：N/S/P 摻雜碳 → 單原子催化劑（M-N-C）
- PGM-free 主要挑戰：衰減與耐久性不足

---

## 待辦
- [ ] 補下載 Mølmen et al. APL Mater. 2021 (10.1063/5.0045801)
- [ ] 其餘 review 解析完成後陸續加入
- [ ] AEMFC Fig 5a 讀圖取點
