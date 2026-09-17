# -*- coding: utf-8 -*-
"""图13：对比折线图（2021年/2022年 两条折线对比）"""
from common import setup, save, FG

月份 = ["1月", "2月", "3月", "4月", "5月", "6月"]
年21 = [1686, 1345, 1934, 1658, 1865, 1936]
年22 = [1385, 1846, 1654, 1936, 2564, 2236]

fig, ax = setup()
x = list(range(len(月份)))
ax.plot(x, 年21, color="#E74E69", linewidth=1.5, marker="o",
        markersize=6, markerfacecolor="#E74E69", markeredgecolor="#FFD0D8",
        zorder=3, label="2021年")
ax.plot(x, 年22, color="#0070C0", linewidth=1.5, marker="o",
        markersize=6, markerfacecolor="#0070C0", markeredgecolor="#BFE3FF",
        zorder=3, label="2022年")
for xi, v in zip(x, 年21):
    ax.text(xi, v + 100, f"{v}", ha="center", va="bottom",
            color=FG, fontsize=11, zorder=4)
for xi, v in zip(x, 年22):
    ax.text(xi, v + 100, f"{v}", ha="center", va="bottom",
            color=FG, fontsize=11, zorder=4)

ax.set_xticks(x)
ax.set_xticklabels(月份, color=FG)
ax.set_ylim(1000, 2900)
ax.set_yticks([])
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.legend(loc="upper center", ncol=2, frameon=False, labelcolor=FG,
          fontsize=11, borderaxespad=0.6)
save(fig, "13_对比折线图")
