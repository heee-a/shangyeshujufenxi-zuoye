# -*- coding: utf-8 -*-
"""图1：渐变柱形图（复刻自 第二章 图表(前15).xlsx 第1张表）"""
from common import setup, save, gradient_bar, BG, FG

区域 = ["华北", "华南", "东北", "西北", "西南", "华东"]
销量 = [2354, 1902, 3524, 2698, 2896, 2563]

fig, ax = setup()
x = list(range(len(区域)))
w = 0.42
for xi, v in zip(x, 销量):
    gradient_bar(ax, xi - w / 2, 0, w, v, "#0070C0", "#00B0F0")  # 底深顶浅
    ax.text(xi, v + 90, f"{v}", ha="center", va="bottom",
            color=FG, fontsize=11, zorder=4)

ax.set_xticks(x)
ax.set_xticklabels(区域, color=FG)
ax.set_ylim(0, 4100)
ax.set_yticks([0, 1000, 2000, 3000, 4000])
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
save(fig, "01_渐变柱形图")
