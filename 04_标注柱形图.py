# -*- coding: utf-8 -*-
"""图4：标注柱形图（不同颜色的柱形 + 数值标注）"""
from common import setup, save, FG

商品 = ["口红", "面膜", "隔离", "防晒", "精华", "面霜", "眼影", "气垫"]
销量 = [9221, 5102, 6571, 5760, 6321, 8612, 2645, 5321]
颜色 = ["#7BBDD5", "#49A098", "#E66B4C", "#FFC000",
        "#0097E0", "#0070C0", "#4A5BD1", "#464CAC"]

fig, ax = setup()
x = list(range(len(商品)))
ax.bar(x, 销量, width=0.55, color=颜色, zorder=3)
for xi, v in zip(x, 销量):
    ax.text(xi, v + 200, f"{v}", ha="center", va="bottom",
            color=FG, fontsize=11, zorder=4)

ax.set_xticks(x)
ax.set_xticklabels(商品, color=FG)
ax.set_ylim(0, 10800)
ax.set_yticks([0, 3000, 6000, 9000])
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
save(fig, "04_标注柱形图")
