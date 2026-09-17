# -*- coding: utf-8 -*-
"""图3：渐变圆角柱形图（圆角顶部的渐变细柱）"""
from common import setup, save, gradient_bar, FG

商品 = ["口红", "面膜", "隔离", "防晒", "精华", "面霜"]
销量 = [653, 523, 648, 856, 714, 785]

fig, ax = setup()
x = list(range(len(商品)))
w = 0.25
for xi, v in zip(x, 销量):
    gradient_bar(ax, xi - w / 2, 0, w, v, "#00509F", "#00F3FC", rounded=True)
    ax.text(xi, v + 40, f"{v}", ha="center", va="bottom",
            color=FG, fontsize=11, zorder=4)

ax.set_xticks(x)
ax.set_xticklabels(商品, color=FG)
ax.set_ylim(0, 1200)
ax.set_yticks([0, 300, 600, 900, 1200])
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
save(fig, "03_渐变圆角柱形图")
