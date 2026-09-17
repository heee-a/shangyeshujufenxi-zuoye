# -*- coding: utf-8 -*-
"""图5：层叠柱形图（销售额与利润额，柱间部分重叠）"""
from common import setup, save, FG

季度 = ["2021Q1", "Q2", "Q3", "Q4", "2022Q1", "Q2"]
销售额 = [3121, 4086, 4321, 4601, 4936, 4231]
利润额 = [1020, 1421, 1502, 1623, 1781, 1432]

fig, ax = setup()
x = list(range(len(季度)))
w = 0.42
ax.bar(x, 销售额, width=w, color="#0070C0", zorder=3)
ax.bar([xi + 0.7 * w for xi in x], 利润额, width=w, color="#E74E69", zorder=4)
for xi, v in zip(x, 销售额):
    ax.text(xi, v + 150, f"{v}", ha="center", va="bottom",
            color=FG, fontsize=11, zorder=5)
for xi, v in zip(x, 利润额):
    ax.text(xi + 0.7 * w, v + 150, f"{v}", ha="center", va="bottom",
            color=FG, fontsize=11, zorder=5)

ax.set_xticks([xi + 0.35 * w for xi in x])
ax.set_xticklabels(季度, color=FG)
ax.set_ylim(0, 5600)
ax.set_yticks([])          # 原图不显示数值轴
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
save(fig, "05_层叠柱形图")
