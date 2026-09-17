# -*- coding: utf-8 -*-
"""图17：玉玦图（四层同心圆弧，弧长代表占比，弧间缺口如玦）"""
from matplotlib.patches import Wedge
from common import setup, save, FG

# 由外到内的四层环：类别、占比、颜色
环 = [
    ("≥50岁", 0.125, "#37A2DA"),
    ("[40,50)", 0.208333, "#11A7AD"),
    ("[30,40)", 0.291667, "#F5C353"),
    ("[20,30)", 0.375, "#E74E69"),
]

fig, ax = setup(6.8, 6.0, margins=(0.04, 0.06, 0.96, 0.92))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect("equal")
ax.axis("off")

cx, cy = 0.5, 0.47
R_out = 0.36
R_in = R_out * 0.35                     # holeSize 35%
n = len(环)
rw = (R_out - R_in) / n

for i, (name, frac, color) in enumerate(环):
    r1 = R_out - i * rw
    r2 = r1 - rw
    span = frac * 360
    t1 = (90 - span) % 360             # Excel 角度 0 起（12 点方向）顺时针
    t2 = 90
    ax.add_patch(Wedge((cx, cy), r1, theta1=t1, theta2=t2, width=rw,
                       facecolor=color, edgecolor="#1A1E43", linewidth=0.8))
    # 弧起点处（12 点方向）标注类别与占比，沿半径竖排
    ax.text(cx - 0.015, cy + (r1 + r2) / 2, f"{name}  {frac:.1%}",
            ha="right", va="center", color=color, fontsize=10)

ax.text(cx, cy, "玉玦图", ha="center", va="center", color="#8888AA",
        fontsize=13)
save(fig, "17_玉玦图")
