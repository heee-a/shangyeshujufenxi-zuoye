# -*- coding: utf-8 -*-
"""图26：柱形圆（柱顶上方圆圈标注同比值）"""
from matplotlib.patches import Circle
from common import setup, save, FG

区域 = ["华北", "华南", "东北", "西北", "西南", "华东"]
销量 = [2354, 1902, 3524, 2698, 2896, 2563]
同比 = [0.12, 0.25, 0.16, 0.21, 0.18, 0.25]

fig, ax = setup()
x = list(range(len(区域)))
ax.bar(x, 销量, width=0.42, color="#E74E69", zorder=3)
for xi, v in zip(x, 销量):
    ax.text(xi, v + 90, f"{v}", ha="center", va="bottom",
            color=FG, fontsize=11, zorder=4)
# 柱顶上方圆圈（蓝圈 + 同比标签）
top = 4500
for xi, t in zip(x, 同比):
    ax.add_patch(Circle((xi, top), 0.30, facecolor="#0070C0",
                        edgecolor="none", zorder=4))
    ax.text(xi, top, f"{t:.0%}", ha="center", va="center",
            color=FG, fontsize=9, zorder=5)

ax.set_xticks(x)
ax.set_xticklabels(区域, color=FG)
ax.set_ylim(0, 4600)
ax.set_yticks([])
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
save(fig, "26_柱形圆")
