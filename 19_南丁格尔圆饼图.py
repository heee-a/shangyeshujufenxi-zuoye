# -*- coding: utf-8 -*-
"""图19：南丁格尔圆饼图（各扇区按占比错层展开的玫瑰饼图）"""
import numpy as np
from matplotlib.patches import Wedge
from common import setup, save, FG

# (部门, 占比, 颜色, 扇区半径范围[内,外])
扇区 = [
    ("销售部", 0.292, "#E74E69", (0.00, 238)),   # 销售部为从圆心开始的完整扇形
    ("采购部", 0.227, "#F5C353", (238, 290)),
    ("工程部", 0.175, "#11A7AD", (186, 238)),
    ("财务部", 0.136, "#0070C0", (145, 212)),
    ("行政部", 0.103, "#37A2DA", (160, 239)),
    ("人力部", 0.067, "#7030A0", (210, 274)),
]
R_MAX = 290
# 绘制顺序：先画大的（底层），后画小的（顶层）
绘制顺序 = [("人力部", "#7030A0", (210, 274)), ("行政部", "#37A2DA", (160, 239)),
            ("财务部", "#0070C0", (145, 212)), ("工程部", "#11A7AD", (186, 238)),
            ("采购部", "#F5C353", (238, 290)), ("销售部", "#E74E69", (0, 238))]

fig, ax = setup(7.4, 6.4, margins=(0.04, 0.06, 0.96, 0.92))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect("equal")
ax.axis("off")

cx, cy = 0.5, 0.47
scale = 0.38 / R_MAX                     # 像素半径 → 坐标

# 各扇区 Excel 角度范围（自 12 点方向顺时针）
e = 0
角度表 = {}
for name, frac, color, _ in 扇区:
    角度表[name] = (e, e + frac * 360)
    e += frac * 360

for name, color, (r1, r2) in 绘制顺序:
    e0, e1 = 角度表[name]
    t1 = (90 - e1) % 360
    t2 = (90 - e0) % 360
    ax.add_patch(Wedge((cx, cy), r2 * scale, theta1=t1, theta2=t2,
                       width=(r2 - r1) * scale, facecolor=color,
                       edgecolor="none"))

# 标签 + 引导线
for name, frac, color, _ in 扇区:
    e0, e1 = 角度表[name]
    mid = (e0 + e1) / 2
    rad = np.radians(mid)
    lx = cx + 0.30 * np.sin(rad)
    ly = cy + 0.30 * np.cos(rad)
    ax.text(lx, ly, f"{name} {frac:.1%}", ha="center", va="center",
            color=FG, fontsize=10)
ax.text(cx, cy - 0.055, "部门人数占比", ha="center", va="center",
        color="#8888AA", fontsize=11)
save(fig, "19_南丁格尔圆饼图")
