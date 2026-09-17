# -*- coding: utf-8 -*-
"""图18：跑道图（六层同心圆环，环长代表各部门人数）"""
import numpy as np
from matplotlib.patches import Wedge
from common import setup, save, FG

部门 = ["人力部", "行政部", "财务部", "工程部", "采购部", "销售部"]
人数 = [130, 226, 238, 293, 326, 451]
颜色 = ["#7030A0", "#0070C0", "#37A2DA", "#11A7AD", "#F5C353", "#E74E69"]
总数 = 832

fig, ax = setup(6.8, 6.2, margins=(0.04, 0.06, 0.96, 0.92))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect("equal")
ax.axis("off")

cx, cy = 0.5, 0.48
R_out = 0.38
R_in = R_out * 0.45                     # holeSize 45%
n = len(部门)
rw = (R_out - R_in) / n

for i, (name, v, color) in enumerate(zip(部门, 人数, 颜色)):
    r1 = R_out - i * rw
    r2 = r1 - rw
    span = v / 总数 * 360
    t1 = (90 - span) % 360
    t2 = 90
    ax.add_patch(Wedge((cx, cy), r1, theta1=t1, theta2=t2, width=rw,
                       facecolor=color, edgecolor="#1A1E43", linewidth=0.8))
    # 弧尾标签：名称+人数（弧尾 = 自 12 点顺时针 span 度处）
    rad = np.radians(span)
    lx = cx + (R_out + 0.085) * np.sin(rad)
    ly = cy + (R_out + 0.085) * np.cos(rad)
    ax.text(lx, ly, f"{name} {v}", ha="center", va="center",
            color=color, fontsize=10)

ax.text(cx, cy, "跑道图", ha="center", va="center", color="#8888AA",
        fontsize=13)
save(fig, "18_跑道图")
