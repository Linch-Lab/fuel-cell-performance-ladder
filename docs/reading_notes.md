# FC Review 閱讀筆記

> 燃料電池性能天梯（fuel-cell-performance-ladder）文獻閱讀彙整
> 更新：2026-08-09

---

## R11. GDL Review (2026 Energy & Fuels) ✅ 已讀

**文獻**：Li et al. (2026). "A Review of Gas Diffusion Layers in PEM Fuel Cells: Bridging Commercial Scalability and Structural Optimization." *Energy & Fuels* 40, 13223-13253
**狀態**：✅ MinerU 解析 + 深讀完成（810 行）

### 關鍵數據
- GDL 優化後峰值功率密度可達 **~1.7 W/cm²**
- 學術 MPL：~1.2 W/cm² 但壽命 <500h；商用 MPL：>5000h
- 碳紙成本 $20-50/m²；Ti foam 密度 1.2-1.8 g/cm³
- 1325 篇文獻系統回顧（2010-2025）

---

## R12. Pt-Ni Nanoalloy (2026 JES) ✅ 已讀

**文獻**：Amarlou et al. (2026). "Breaking the Bottleneck: Pt–Ni Nanoalloys as Next-Generation Catalysts for ORR in PEMFC." *J. Electrochem. Soc.* 173, 096502
**狀態**：✅ MinerU 解析 + 深讀完成（508 行）

### 關鍵數據（半電池，尚未到單電池）
- **Pt₁Ni₈@NC**：質量活性 **2.02 A/mg_Pt @0.9V**（9× 商用 Pt/C 0.22）
- 比活性 2.88 mA/cm²（9.3×）；ECSA 69.9 m²/g
- 30,000 cycles 後質量活性僅損失 9.9%（Pt/C >45%）
- ΔE₁/₂ 僅 9 mV（Pt/C 42 mV）
- ⚠️ 僅半電池驗證——單電池極化/功率密度待確認

---

## C1. 商業 SOFC — Bloom Energy（2026-08 收集）✅

| 產品/系統 | 電效率%(基準) | CHP% | 功率 | 年份 | 來源 |
|------|:--:|:--:|:--:|:--:|------|
| Bloom H₂ SOFC 平台 | **60%**（BOL, 100% H₂）| **90%**（高溫 CHP）| — | 2024 | bloomenergy.com 新聞稿 (2024-08-05) |
| Bloom Energy Server（H₂）| 52%（LHV, net AC）| — | 300 kW | 2022 | hydrogen-data-sheet.pdf |
| Bloom Series 10 | — | CHP 5 MWt @>350°C | 10 MW | 2023 | Series10-V12.pdf |

- 原始 PDF 存：`ref/commercial/`（Bloom_H2_DataSheet_2022、Bloom_Series10_2023、Bloom_H2_Blending_TechnicalNote）
- 未驗證（勿引用）：Doosan PureCell 400、Mitsubishi SOFC-MGT、Sunfire、Aisin Ene-Farm 46.5%、Jülich 70,000h

---

## R13. PEMFC 膜文獻計量 (2026 JMEP) ✅ 已讀

**文獻**：Kesercioğlu et al. (2026). "Sustainable Membrane Materials in PEM Fuel Cells: A Bibliometric Analysis." *J. Mater. Eng. Perform.*
**狀態**：✅ MinerU 解析 + 深讀完成（370 行）

### 關鍵結論
- 1991-2025 PEMFC 膜研究文獻計量分析
- 2017 後研究量激增（氫能政策驅動）
- 主題轉向：無氟膜、生物基材料、高溫耐久
- 中國居研究量/引用首位

---

## R10. Metal Oxide Support Review (2026 CEJ) ✅ 已讀

**文獻**：Vishnudhatha K B et al. (2026). "Recent Progress in metal oxide support materials for ORR in PEMFC." *Chem. Eng. J.*
**狀態**：✅ MinerU 解析 + 深讀完成（1236 行）

### 最高性能（Table 4，年份待追）

| 催化劑 | PPD (mW/cm²) | 0.6V (mA/cm²) | Pt (mg/cm²) | 氣體 |
|------|:--:|:--:|:--:|:--:|
| **Pt-CNT@SnO₂** | **1618** | 2225 | 0.096 | H₂/O₂ |
| Pt/Zr-ECS | 1405 | 2342 | 0.2 | H₂/air |
| **Pt/ZrO₂₋ₓ** | **1270** | 2025 | 0.15 | H₂/air |
| Pt/C@N-TiO₂ | 1300 | 1648 | NA | H₂/O₂ |
| Pt/PT-SSO | 1173 | 1590 | 0.3 | H₂/O₂ |
| Pt/TiO₂₋ₓ | 1170 | 1831 | 0.15 | H₂/air |
| ALD-TaOx-Pt/C | 1080 | 1591 | 0.15 | H₂/air |
| CoOx@Pt/C | 1040 | 1915 | 0.1 | H₂/air |

### 關鍵結論
- 最高 PPD 1618 mW/cm²（Pt-CNT@SnO₂，極低 Pt 0.096）
- 金屬氧化物載體耐久性大幅優於碳（30k cycles <12% vs 19.8%）
- H₂/air 最高 1405（Pt/Zr-ECS）

---

## R9. LT-SOFC Review (2024 JPS) ✅ 已讀

**文獻**：(2024). "Advances in low-temperature solid oxide fuel cells: An explanatory review." *J. Power Sources*
**狀態**：✅ MinerU 解析 + 深讀完成（845 行）

### 低溫 SOFC 性能數據點（年份待追）

| 峰值功率 (mW/cm²) | 溫度 | 配置 |
|:--:|:--:|------|
| **2000** | 650°C | ESB/GDC 雙層電解質 |
| 1950 | 600°C | Fe 摻雜 Ni 陽極 + LSGM |
| 1257 | 520°C | ZnO/NiO-SDC 複合陽極 |
| 1200 | 500°C | SCNT 鈣鈦礦陰極 |
| 700 | 450°C | SCNT 陰極 |
| 600 | 550°C | Li₄Ti₅O₁₂ 三導體 |
| 564 | 750°C | Ni-BZCYYb（丙烷）|
| 493 | 500°C | 薄膜 YSZ |
| 431 | 600°C | SNS 電解質 |
| 225 | — | H-SNO 質子導體 |

### 關鍵結論
- 低溫化趨勢：500°C 已達 1200 mW/cm²
- ESB/GDC 雙層 650°C → 2 W/cm² 創紀錄
- 奈米化陽極是低溫關鍵

---

## R6. SOFC Decade Review (2021 IJHE) ✅ 已讀

**文獻**：(2021). "Solid oxide fuel cell: Decade of progress, future perspectives and challenges." *Int. J. Hydrogen Energy* DOI: 10.1016/j.ijhydene.2021.06.020
**狀態**：✅ MinerU 解析 + 深讀完成（967 行）

### O-SOFC 性能數據點（年份待追原始文獻）

| 峰值功率 (W/cm²) | 溫度 | 配置 |
|:--:|:--:|------|
| **2.5** | 900°C | 浸漬電極 |
| 1.75 | 800°C | 陽極孔結構優化 |
| 1.69 | 800°C | LNO-LSC 梯度層 |
| 1.3 | 700°C | 浸漬電極 |
| 1.12 | 650°C | Sn 摻雜 Ni-GDC 陽極 |
| 0.93 | 650°C | 同上，CH₄ |
| 0.848 | 800°C | BSFA-GDC 陰極 |
| 0.572 | 850°C | 碳微球孔形成劑 |
| 0.508 | 800°C | NiO-CZ50 陽極 |
| 0.45 | 810°C | PIM 製備 |

### 關鍵結論
- 陽極支撐 SOFC 最高 2.5 W/cm²（900°C）
- 650°C 低溫仍可 1.12 W/cm²
- P-SOFC（電解質支撐）：性能較差但電流分佈最均勻

---

## R8. PEMFC Developments Review (2025 Chem Commun) ✅ 已讀

**文獻**：(2025). "Proton exchange membrane fuel cells: recent developments and future perspectives." *Chem. Commun.* DOI: 10.1039/d5cc01478f
**狀態**：✅ MinerU 解析 + 深讀完成（791 行）

### 關鍵數據點
| 項目 | 數值 |
|------|:--:|
| Mirai 2 電堆功率密度 | 5.4 kW/L（+54% vs 前代）|
| Pt-Sc/PECNT 陰極 | 760 mW/cm² |
| PEMFC 效率 | 40–60% |
| Nafion 膜成本 | ~$2000/m² |
| GDL 減薄 82% | 提升體積功率密度 |

### PGM-free 進展
- Fe-N-C、CoNC-900（OER 210 mV vs RuO₂ 280 mV）、N-doped graphene

### 天梯數據（PEMFC）
- Pt-Sc/PECNT 760 mW/cm²（原始年份待查）

---

## R4. Pt Utilization Review (2022 Chem Soc Rev) ✅ 已讀

**文獻**：(2022). "Pt utilization in proton exchange membrane fuel cells: structure impacting factors and mechanistic insights." *Chem. Soc. Rev.* DOI: 10.1039/d1cs00981h
**狀態**：✅ MinerU 解析 + 深讀完成（569 行）

### 核心機制
- **R_local（離聚物薄膜 O₂ 傳輸阻抗）**：低 Pt 載量（<0.1 mg/cm²）高電流區（>1 A/cm²）性能陡降主因
- 離聚物薄膜厚度 6–13 nm（AFM）
- NSTF 電極（無離聚物）R_NF=0.1 s/cm；覆 2-4nm 離聚物後 0.5–1 s/cm

### 關鍵公式
- R_total = R_CL^Knudsen + R_local + p/B
- R_local = R_O2^Pt/(A_Pt·m_Pt)

### 對天梯意義
- 低 Pt 化代價 = 高電流區質傳損失（PGM 減量 vs 性能 trade-off）

---

## R7. PEMFC 氣體交叉 Review (2026 Applied Energy) ✅ 已讀

**文獻**：Yang et al. (2026). "Analysis of operating condition parameters induced gas crossover phenomenon in PEM fuel cells: A review." *Applied Energy*
**狀態**：✅ MinerU 解析 + 深讀完成（619 行）

### 核心因果鏈
操作參數（溫度/濕度/流量）→ 元件退化（膜/CL/GDL）→ 氣體交叉加劇 → 性能與安全惡化（惡性循環）

### 關鍵量化數據
| 項目 | 數值 |
|------|:--:|
| 化學退化膜厚度損失 | 30–70% |
| Fe²⁺/Cu²⁺ 催化自由基 | 產率增 1-2 數量級、針孔成長快 3-5 倍 |
| 濕度循環峰值機械應力 | 2.23 MPa |
| 儲存濕度波動（致膜皺褶）| 20–75% RH |

### 對天梯意義
- 薄膜 vs 氣體交叉 trade-off：解釋高性能薄膜壽命短
- 可作為資料庫衰退註記欄位來源

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
