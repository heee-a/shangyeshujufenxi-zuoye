# -*- coding: utf-8 -*-
"""图7：蝴蝶图（REPT 公式单元格条形图，=REPT("|",值*200)）
原图用 Excel 单元格公式直接生成竖线条形，这里用 matplotlib 复刻同样的效果。"""
from common import setup, save, FG

区域 = ["华东", "西北", "东北", "华北", "华南"]
年22 = [0.36, 0.31, 0.18, 0.13, 0.09]   # 2022年（左，蓝）
年21 = [0.42, 0.26, 0.19, 0.12, 0.05]   # 2021年（右，红）

fig, ax = setup(8.8, 6.2)
y = list(range(len(区域)))[::-1]
maxlen = 0.5
for yi, v22, v21, name in zip(y, 年22, 年21, 区域):
    # 左侧 2022年（蓝色竖线组）
    n = int(v22 * 200)
    xs = [i / 200 for i in range(1, n + 1)]
    ax.vlines(xs, yi - 0.32, yi + 0.32, colors="#0070C0",
              linewidths=1.6, zorder=3)
    ax.text(-0.005, yi, f"{v22:.0%}", va="center", ha="right",
            color="#4FC3F7", fontsize=11)
    # 右侧 2021年（红色竖线组）
    n = int(v21 * 200)
    xs = [maxlen + i / 200 for i in range(1, n + 1)]
    ax.vlines(xs, yi - 0.32, yi + 0.32, colors="#E74E69",
              linewidths=1.6, zorder=3)
    ax.text(maxlen * 2 + 0.005, yi, f"{v21:.0%}", va="center", ha="left",
            color="#FF8A9A", fontsize=11)
    # 中间区域名
    ax.text(maxlen, yi, name, va="center", ha="center",
            color=FG, fontsize=12, zorder=5)

ax.text(maxlen, len(区域) - 0.55, "2022年", color="#4FC3F7",
        fontsize=13, ha="center", va="center")
ax.text(maxlen, len(区域) + 0.05, "2021年", color="#FF8A9A",
        fontsize=13, ha="center", va="center")

ax.set_xlim(-0.08, maxlen * 2 + 0.08)
ax.set_ylim(-0.75, len(区域) + 0.35)
ax.set_yticks([])
ax.set_xticks([])
for s in ax.spines.values():
    s.set_visible(False)
save(fig, "07_蝴蝶图REPT公式")
