# -*- coding: utf-8 -*-
"""图20：南丁格尔圆环图（五层圆环，每层扇区数递减）"""
import numpy as np
from matplotlib.patches import Wedge
from common import setup, save, FG

# 年龄组（自 12 点方向顺时针）：占比、颜色
组 = [
    ("[20,30)", 0.375, "#512DCB"),
    ("[30,40)", 0.291667, "#6073F3"),
    ("[40,50)", 0.208333, "#66CBDD"),
    ("≥50", 0.125, "#F5C353"),
]
# 各层圆环包含前几个扇区（由外到内）
层 = [4, 4, 3, 2, 1]

fig, ax = setup(7.0, 6.4, margins=(0.04, 0.06, 0.96, 0.92))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect("equal")
ax.axis("off")

cx, cy = 0.5, 0.47
R_out = 0.38
R_in = R_out * 0.60                     # holeSize 60%
n = len(层)
rw = (R_out - R_in) / n

# 各扇区 Excel 角度范围
e = 0
角度 = []
for name, frac, color in 组:
    角度.append((e, e + frac * 360))
    e += frac * 360

for i, cnt in enumerate(层):
    r1 = R_out - i * rw
    r2 = r1 - rw
    for j in range(cnt):
        e0, e1 = 角度[j]
        t1 = (90 - e1) % 360
        t2 = (90 - e0) % 360
        ax.add_patch(Wedge((cx, cy), r1, theta1=t1, theta2=t2, width=rw,
                           facecolor=组[j][2], edgecolor="#101040", linewidth=0.5))

# 最内层扇区标注（类别+占比，放在孔内）
for j, (name, frac, color) in enumerate(组):
    e0, e1 = 角度[j]
    mid = (e0 + e1) / 2
    rad = np.radians(mid)
    lx = cx + (R_in - 0.06) * np.sin(rad)
    ly = cy + (R_in - 0.06) * np.cos(rad)
    ax.text(lx, ly, f"{name}\n{frac:.1%}", ha="center", va="center",
            color=color, fontsize=9.5)

ax.text(cx, cy, "年龄分布", ha="center", va="center", color="#8888AA",
        fontsize=11)
save(fig, "20_南丁格尔圆环图")
