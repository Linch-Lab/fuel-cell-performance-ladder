# 商業 PEMFC/SOFC 系統性能資料（2016–2026）

> fuel-cell-performance-ladder 專案 COMMERCIAL 技術線資料
> 收集：2026-08-09（官方來源驗證）

## 車用 PEMFC

| 車型/產品 | 世代 | 電堆功率(kW) | 電堆密度(kW/L) | 系統密度(W/L) | 峰值效率%(LHV) | 年份 | 來源 | 備註 |
|---|---|---|---|---|---|---|---|---|
| Toyota Mirai 一代 | 第1代 | 114 gross | 3.1 | 640* | **64%**（ANL 實測）| 2014/2020 | DOE Record 20005 + toyota.co.jp | 370 節、3D fine-mesh、2.0 kW/kg、PGM ~0.3 g/kW |
| Toyota Mirai 二代 (FCB130) | 第2代 | 128 gross (+12%) | **5.4**（不含端板，世界紀錄）| — | 未公布 | 2020 | toyota.eu + global.toyota | 330 節、系統重量 −50% |
| Honda Clarity FC | 第2代 V-Flow | ~100 ⚠️ | 較前代 +60% ⚠️ | — | — | 2016 | hondanews wayback | 電堆縮小 33%、量產平台車 |
| Honda CR-V e:FCEV | 第3代（GM 合作）| **92.2**（模組）| — | — | — | 2024 | hondanews wayback | 美國首款量產 FCEV、成本降 2/3 |
| Hyundai Nexo 1代 | 2018 | **95** | — | — | — | 2018 | hyundainews wayback | 370 mi、5 分鐘加氫 |
| Hyundai Nexo 2代 | 2025 | — | — | — | — | 2025 | Wikipedia | 馬達 190 kW、WLTP ~700 km |
| BMW iX5 Hydrogen | Toyota 合作 | 125 ⚠️ | — | — | — | 2021/2023 | BMW 2022 年報 | ~100 台試量產、2023 試營運 |

## 固定式 PEMFC（Ene-Farm）

| 產品 | 技術 | 功率 | 電效率%(LHV) | 總效率% | 年份 | 來源 | 備註 |
|---|---|---|---|---|---|---|---|
| Panasonic エネファーム FC-70NR13T-1 | PEM（改質 NG）| 0.7 kW | **41.0** (37.0 HHV) | 熱 57.0 → 總合 ~91 | 2019– | panasonic.biz | 日本家用 FC 基準 |
| Panasonic 大容量貯湯型 | PEM | 0.7 kW | 40.0 | 熱 61.0 | 2019– | panasonic.biz | — |

## 高溫固定式（SOFC/MCFC/PAFC）

| 產品 | 技術 | 功率 | 電效率% | 總效率% | 年份 | 來源 | 備註 |
|---|---|---|---|---|---|---|---|
| Bloom H₂ SOFC | SOFC | 模組化 | **60**（LHV, 100% H₂）| **90** CHP | 2024 | bloomenergy.com | 2024-08-05 官方新聞稿 |
| Bloom Energy Server H₂ | SOFC | 300 kW | 52（LHV net AC）| — | 2022 | hydrogen-data-sheet.pdf | H₂ 消耗 17.3 kg/hr |
| Bloom Series 10 | SOFC | 10 MW | — | CHP 5 MWt | 2023 | Series10-V12.pdf | NG/RNG/H₂/混合 |
| FuelCell Energy SureSource 4000 | MCFC | 3.7 MW | **~60**（LHV AC 淨）| — | 2020 | globenewswire + FCE blog | 2020-04 商業運轉 |
| FuelCell Energy SureSource 3000 | MCFC | 2.8 MW | ~47 | — | 2019 | 產品規格 wayback | 2×1.4 MW |
| Doosan PureCell M400 (NG) | PAFC | 440 kW | 43 | 90（+熱 47）| 2023– | doosanfuelcell.com | — |
| Doosan PureCell M400 (H₂) | PAFC | 440 kW | **50** | 85（+熱 35）| 2023– | doosanfuelcell.com | 純氫最高 |
| Doosan PureCell M400 (LPG/NG) | PAFC | 440 kW | 41/43 | 90 | 2023– | doosanfuelcell.com | — |
| Aisin/Toshiba エネファーム (SOFC) | SOFC | 0.7 kW | **46.5** ⚠️ | — | 2012– | ja-wiki + aisin.com | 46.5% 需複核 |

## ⚠️ 未驗證項目
- BMW 電堆 125 kW（PressClub 需登入）
- Aisin SOFC 46.5%
- Bloom ES5-200 kW 規格頁
- Honda Clarity 電堆絕對 kW

## 來源檔案
- `ref/commercial/`：Bloom_H2_DataSheet_2022.pdf、Bloom_Series10_2023.pdf、Bloom_H2_Blending_TechnicalNote.pdf
- `/tmp/fc/`：bmw_r2022_wb.pdf、anl_mirai.pdf、fce_ss3000/4000.pdf、bloom_10k.htm
