# -*- coding: utf-8 -*-
"""图21：南丁格尔（PPT）风格饼图（带引导线的部门人数占比饼图）"""
import numpy as np
from common import setup, save, FG

部门 = ["销售部", "采购部", "工程部", "财务部", "行政部", "人力部"]
占比 = [0.292, 0.227, 0.175, 0.136, 0.103, 0.05]
颜色 = ["#5B9BD5", "#ED7D31", "#A5A5A5", "#FFC000", "#4472C4", "#70AD47"]

fig, ax = setup(7.4, 6.4, margins=(0.04, 0.06, 0.96, 0.90))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect("equal")
ax.axis("off")

cx, cy = 0.5, 0.46
R = 0.27

# 自 12 点方向顺时针画各扇区
e = 0
mids = []
for name, frac, color in zip(部门, 占比, 颜色):
    t1 = (90 - (e + frac * 360)) % 360
    t2 = (90 - e) % 360
    from matplotlib.patches import Wedge
    ax.add_patch(Wedge((cx, cy), R, theta1=t1, theta2=t2,
                       facecolor=color, edgecolor="#101040", linewidth=1))
    mids.append(e + frac * 180)
    e += frac * 360

# 标签引导线
for (name, frac, color), mid in zip(zip(部门, 占比, 颜色), mids):
    rad = np.radians(mid)
    sx, sy = cx + R * np.sin(rad), cy + R * np.cos(rad)
    lx, ly = cx + (R + 0.09) * np.sin(rad), cy + (R + 0.09) * np.cos(rad)
    ax.plot([sx, lx], [sy, ly], color="#8888AA", linewidth=1, zorder=2)
    ha = "left" if np.cos(rad) >= -0.2 else "right"
    ax.text(lx + 0.012 * np.sign(np.sin(rad) or 1) * (1 if ha == "left" else -1),
            ly, f"{name} {frac:.1%}", ha=ha, va="center",
            color=FG, fontsize=10)

# 标题与注释
ax.text(0.5, 0.95, "2021年各部门人数分布", ha="center", va="center",
        color=FG, fontsize=15, fontweight="bold")
ax.text(0.5, 0.88, "公司总人数1664，销售部人数最多451，占比29.2%",
        ha="center", va="center", color="#C9C9DD", fontsize=11)
ax.text(0.5, 0.03, "*注：数据来源于公司人力资源系统，统计日期截至2022.01.01",
        ha="center", va="center", color="#8888AA", fontsize=9)
save(fig, "21_南丁格尔PPT风格饼图")
