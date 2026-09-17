# -*- coding: utf-8 -*-
"""图15：水球图（蓝色圆球 + 65% 完成率，原图为 条形图+椭圆形状 组合）"""
from matplotlib.patches import Circle
from common import setup, save, FG

fig, ax = setup(7.0, 6.0, margins=(0.04, 0.06, 0.96, 0.90))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect("equal")
ax.axis("off")

cx, cy = 0.5, 0.47
R = 0.30
# 水球（实心蓝圆）+ 外圈
ax.add_patch(Circle((cx, cy), R, facecolor="#0070C0", edgecolor="none", zorder=3))
ax.add_patch(Circle((cx, cy), R * 1.10, facecolor="none",
                    edgecolor="#0070C0", linewidth=2, zorder=3))
# 小装饰圆
ax.add_patch(Circle((cx + R * 1.35, cy + R * 0.9), R * 0.11, facecolor="none",
                    edgecolor="#0070C0", linewidth=2, zorder=3))
# 中心文字
ax.text(cx, cy, "65%", ha="center", va="center", color=FG,
        fontsize=40, fontweight="bold", zorder=4)
# 标题与注释
ax.text(0.5, 0.94, "2022年上半年目标完成率", ha="center", va="center",
        color=FG, fontsize=15, fontweight="bold")
ax.text(0.5, 0.87, "截至6月30日，销售目标总体完成率达到65%", ha="center",
        va="center", color="#C9C9DD", fontsize=11)
ax.text(0.5, 0.035, "*注：数据来源于公司销售系统", ha="center", va="center",
        color="#8888AA", fontsize=9)
save(fig, "15_水球图")
