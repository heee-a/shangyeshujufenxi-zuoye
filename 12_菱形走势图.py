# -*- coding: utf-8 -*-
"""图12：菱形走势图（菱形标记折线，隐藏数值轴）"""
from common import setup, save, FG

月份 = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月"]
完成率 = [0.536, 0.498, 0.527, 0.708, 0.609, 0.496, 0.586, 0.704]

fig, ax = setup()
x = list(range(len(月份)))
ax.plot(x, 完成率, color="#5B9BD5", linewidth=2.25,
        marker="D", markersize=7, markerfacecolor="#5B9BD5",
        markeredgecolor="#D6EBFF", zorder=3)
for xi, v in zip(x, 完成率):
    ax.text(xi, v + 0.035, f"{v}", ha="center", va="bottom",
            color=FG, fontsize=11, zorder=4)

ax.set_xticks(x)
ax.set_xticklabels(月份, color=FG)
ax.set_ylim(0.35, 0.82)
ax.set_yticks([])
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
save(fig, "12_菱形走势图")
