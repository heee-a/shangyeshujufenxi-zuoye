# -*- coding: utf-8 -*-
"""图16：波浪水球图（圆球 + 波浪水面 + 65% 完成率）"""
import numpy as np
from matplotlib.patches import Circle, PathPatch
from matplotlib.path import Path
from common import setup, save, FG

fig, ax = setup(7.0, 6.0, margins=(0.04, 0.06, 0.96, 0.90))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect("equal")
ax.axis("off")

cx, cy = 0.5, 0.45
R = 0.30
level = cy + R * (2 * 0.65 - 1)      # 65% 水位线

# 水面填充（矩形 + 双波形顶边，裁剪在圆内）
x = np.linspace(cx - R, cx + R, 200)
wave_top = level + 0.012 * np.sin(2 * np.pi * (x - cx + R) / (2 * R) * 2)
verts = [(cx - R, cy - R)]
verts += list(zip(x, wave_top))
verts += [(cx + R, cy - R), (cx - R, cy - R)]
water = PathPatch(Path(verts), facecolor="#0070C0", edgecolor="none", zorder=2)
circle = Circle((cx, cy), R)
water.set_clip_path(circle)

ax.add_patch(circle)
ax.add_patch(water)
# 圆外圈
ax.add_patch(Circle((cx, cy), R * 1.06, facecolor="none",
                    edgecolor="#0070C0", linewidth=2, zorder=3))
ax.add_patch(Circle((cx, cy), R * 1.14, facecolor="none",
                    edgecolor="#0070C0", linewidth=1.2, zorder=3))
# 中心文字
ax.text(cx, cy, "65%", ha="center", va="center", color=FG,
        fontsize=40, fontweight="bold", zorder=4)
# 标题与注释
ax.text(0.5, 0.94, "本科及以上学历员工占比", ha="center", va="center",
        color=FG, fontsize=15, fontweight="bold")
ax.text(0.5, 0.87, "6月30日最新统计数据：本科及以上员工占比65%", ha="center",
        va="center", color="#C9C9DD", fontsize=11)
ax.text(0.5, 0.035, "*注：数据来源于公司人力资源系统", ha="center", va="center",
        color="#8888AA", fontsize=9)
save(fig, "16_波浪水球图")
