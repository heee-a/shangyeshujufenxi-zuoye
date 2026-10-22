# 商业数据分析作业 · 图表绘制练习

商业数据分析课程作业 1：用 **Python（matplotlib）** 复刻 30 张商务图表，统一深色 PPT 设计风格，全部可一键重绘。

图表原型取自课程配套的《第二章 图表(前15).xlsx》，涵盖柱形、折线、饼图、仪表盘、水球图、南丁格尔玫瑰图、滑珠图等常见商务图表类型。

## 特性

- **30 张成品图**：每张一个独立脚本，数据内嵌、开箱即跑
- **统一设计体系**：深色画布 + 蓝色主色板，由 `common.py` 基座统一供给
- **渐变与圆角**：`gradient_bar()` 基于 imshow + 路径裁剪，支持顶部圆角
- **一键重绘**：`python run_all.py` 30 张图约 45 秒全部重出
- **中文字体自适应**：自动探测 Microsoft YaHei / PingFang / Noto CJK，跨平台不出方框

## 快速开始

环境要求：Python 3.8+

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 一键重绘全部图表（约 45 秒）
python run_all.py

# 3. 只重绘其中几张（编号可多选）
python run_all.py 03 15 22
```

单张运行：

```bash
python 03_渐变圆角柱形图.py
```

产物默认写入 `outputs/`（200 dpi PNG，约 1760×1240）。

## 图表画廊

| | | |
|---|---|---|
| ![01](outputs/01_渐变柱形图.png) | ![02](outputs/02_带均值柱形图.png) | ![03](outputs/03_渐变圆角柱形图.png) |
| 01 渐变柱形图 | 02 带均值柱形图 | 03 渐变圆角柱形图 |
| ![04](outputs/04_标注柱形图.png) | ![05](outputs/05_层叠柱形图.png) | ![06](outputs/06_蝴蝶图.png) |
| 04 标注柱形图 | 05 层叠柱形图 | 06 蝴蝶图 |
| ![07](outputs/07_蝴蝶图REPT公式.png) | ![08](outputs/08_数值百分比.png) | ![09](outputs/09_对比柱形图.png) |
| 07 蝴蝶图 REPT 公式 | 08 数值百分比 | 09 对比柱形图 |
| ![10](outputs/10_甘特图.png) | ![11](outputs/11_平滑折线图.png) | ![12](outputs/12_菱形走势图.png) |
| 10 甘特图 | 11 平滑折线图 | 12 菱形走势图 |
| ![13](outputs/13_对比折线图.png) | ![14](outputs/14_单值圆环图.png) | ![15](outputs/15_水球图.png) |
| 13 对比折线图 | 14 单值圆环图 | 15 水球图 |
| ![16](outputs/16_波浪水球图.png) | ![17](outputs/17_玉玦图.png) | ![18](outputs/18_跑道图.png) |
| 16 波浪水球图 | 17 玉玦图 | 18 跑道图 |
| ![19](outputs/19_南丁格尔圆饼图.png) | ![20](outputs/20_南丁格尔圆环图.png) | ![21](outputs/21_南丁格尔PPT风格饼图.png) |
| 19 南丁格尔圆饼图 | 20 南丁格尔圆环图 | 21 南丁格尔 PPT 风格饼图 |
| ![22](outputs/22_仪表盘图.png) | ![23](outputs/23_柱形折线图.png) | ![24](outputs/24_目标柱形图.png) |
| 22 仪表盘图 | 23 柱形折线图 | 24 目标柱形图 |
| ![25](outputs/25_子弹图.png) | ![26](outputs/26_柱形圆.png) | ![27](outputs/27_簇状柱形折线图.png) |
| 25 子弹图 | 26 柱形圆 | 27 簇状柱形折线图 |
| ![28](outputs/28_复合柱形图.png) | ![29](outputs/29_滑珠图.png) | ![30](outputs/30_对比滑珠图.png) |
| 28 复合柱形图 | 29 滑珠图 | 30 对比滑珠图 |

## 设计体系

所有图表共用一套深色 PPT 风格色板（定义于 `common.py`）：

| 角色 | 色值 | 用途 |
|---|---|---|
| BG | `#1A1E43` | 画布背景（深海军蓝） |
| FG | `#E8E8F0` | 主文字 / 刻度 |
| SUB | `#8888AA` | 次级说明文字 |
| GRID | `#2E3560` | 网格线与坐标轴 |
| 主蓝 | `#0070C0` | 主数据系列 |
| 亮蓝 | `#00B0F0` | 渐变顶端 / 高亮 |
| 天蓝 | `#37A2DA` | 辅助系列 |
| 青 | `#11A7AD` | 辅助系列 |
| 黄 | `#F5C353` | 辅助系列 |
| 玫红 | `#E74E69` | 对比 / 负增长系列 |
| 紫 | `#7030A0` | 辅助系列 |

## 项目结构

```
.
├── common.py            # 绘图基座：画布 / 配色 / 渐变柱 / 导出
├── run_all.py           # 一键重绘入口
├── requirements.txt     # 依赖（matplotlib + numpy）
├── 01 ~ 30_*.py         # 30 个独立图表脚本
└── outputs/             # 导出的 PNG 成品图（200 dpi）
```

## common.py 接口速查

```python
from common import setup, save, gradient_bar, BG, FG

# 建画布：figsize 英寸 + (left, bottom, right, top) 边距
fig, ax = setup(8.8, 6.2, margins=(0.08, 0.10, 0.96, 0.94))

# 渐变柱：底深顶浅，rounded=True 时顶部圆角
gradient_bar(ax, x=0, y=0, w=0.42, h=856, c_bottom="#00509F",
             c_top="#00F3FC", rounded=True)

# 导出 200dpi PNG 到 outputs/
save(fig, "03_渐变圆角柱形图")
```

## 常见问题

**Q：图表中文显示为方框？**
A：`common.py` 会按 Microsoft YaHei → PingFang SC → Noto Sans CJK SC → SimHei 的顺序自动探测。Linux 服务器若方框，安装任一 CJK 字体即可（如 `apt install fonts-noto-cjk`）。

**Q：如何改输出目录 / 分辨率？**
A：修改 `common.py` 顶部的 `OUTPUT_DIR` 与 `DPI` 两个常量。

**Q：数据是真的吗？**
A：图表数据为课程练习用的示例数据，内嵌于各脚本中，仅用于绘图练习。

## 许可

课程作业，仅作学习交流使用。
