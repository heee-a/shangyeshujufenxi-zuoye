# -*- coding: utf-8 -*-
"""图24：目标柱形图（白色目标框 + 蓝色实际柱）"""
from common import setup, save, FG

商品 = ["口红", "面膜", "隔离", "防晒", "精华", "面霜"]
实际 = [653, 523, 648, 856, 714, 785]
目标 = [700, 500, 600, 900, 600, 600]

fig, ax = setup()
x = list(range(len(商品)))
# 目标（白色宽框）
ax.bar(x, 目标, width=0.52, color="#E8E8F0", edgecolor="#8888AA",
       linewidth=1.2, zorder=3)
# 实际（蓝色窄柱）
ax.bar(x, 实际, width=0.26, color="#0070C0", zorder=4)
for xi, v, t in zip(x, 实际, 目标):
    ax.text(xi, v + 45, f"{v}", ha="center", va="bottom",
            color=FG, fontsize=11, zorder=5)

ax.set_xticks(x)
ax.set_xticklabels(商品, color=FG)
ax.set_ylim(0, 1000)
ax.set_yticks([])
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
# 底部图例
from matplotlib.patches import Patch
ax.legend(handles=[
    Patch(color="#0070C0", label="实际销量"),
    Patch(facecolor="#E8E8F0", edgecolor="#8888AA", label="目标销量"),
], loc="lower center", bbox_to_anchor=(0.5, -0.14), ncol=2,
   frameon=False, labelcolor=FG, fontsize=11)
save(fig, "24_目标柱形图")
