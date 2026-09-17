# -*- coding: utf-8 -*-
"""图2：带均值柱形图（柱形图 + 均值线）"""
from common import setup, save, FG

区域 = ["华北", "华南", "东北", "西北", "西南", "华东"]
销量 = [2354, 1902, 3524, 2698, 2896, 2563]
均值 = 2656.1666666666665

fig, ax = setup()
x = list(range(len(区域)))
bars = ax.bar(x, 销量, width=0.42, color="#0070C0", zorder=3)
for xi, v in zip(x, 销量):
    ax.text(xi, v + 90, f"{v}", ha="center", va="bottom",
            color=FG, fontsize=11, zorder=4)

ax.plot([-0.5, len(区域) - 0.5], [均值, 均值], color="#FFC000",
        linewidth=1.5, zorder=5, label="均值")
ax.text(len(区域) - 0.5, 均值 + 60, f"均值 {均值:.0f}", ha="right",
        va="bottom", color="#FFC000", fontsize=11)

ax.set_xticks(x)
ax.set_xticklabels(区域, color=FG)
ax.set_ylim(0, 4100)
ax.set_yticks([0, 1000, 2000, 3000, 4000])
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
save(fig, "02_带均值柱形图")
