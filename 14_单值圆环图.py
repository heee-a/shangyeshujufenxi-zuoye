# -*- coding: utf-8 -*-
"""图14：单值圆环图（85% 完成率，紫→红渐变弧）"""
import numpy as np
from matplotlib.patches import Wedge
from common import setup, save, FG

完成率 = 0.85
E_START = 300        # Excel firstSliceAng（自 12 点方向顺时针）
SPAN = 完成率 * 360

fig, ax = setup(6.4, 6.4, margins=(0.05, 0.05, 0.95, 0.95))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect("equal")
ax.axis("off")

cx = cy = 0.5
r_out, r_in = 0.38, 0.38 * 0.90

# 渐变弧（紫→红，自 Excel 角度 300° 顺时针 306°）
c_start, c_end = "#7030A0", "#E74E69"
n = 120
for i in range(n):
    p0, p1 = i / n, (i + 1) / n
    e0 = E_START + SPAN * p0
    e1 = E_START + SPAN * p1
    t1 = (90 - e0) % 360
    t2 = (90 - e1) % 360
    c = tuple(np.array([int(c_start[j:j + 2], 16) for j in (1, 3, 5)]) * (1 - (p0 + p1) / 2)
              + np.array([int(c_end[j:j + 2], 16) for j in (1, 3, 5)]) * ((p0 + p1) / 2))
    ax.add_patch(Wedge((cx, cy), r_out, theta1=t2, theta2=t1, width=r_out - r_in,
                       facecolor=np.array(c) / 255, edgecolor="none"))

# 占位弧（白色 15%）
e0 = E_START + SPAN
e1 = E_START + 360
t1 = (90 - e0) % 360
t2 = (90 - e1) % 360
ax.add_patch(Wedge((cx, cy), r_out, theta1=t2, theta2=t1, width=r_out - r_in,
                   facecolor="#E8E8F0", edgecolor="none"))

ax.text(cx, cy, "85%", ha="center", va="center", color=FG,
        fontsize=46, fontweight="bold")
ax.text(cx, cy - 0.13, "完成率", ha="center", va="center", color="#C9C9DD",
        fontsize=14)
save(fig, "14_单值圆环图")
