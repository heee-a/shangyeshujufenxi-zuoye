# -*- coding: utf-8 -*-
"""图9：对比柱形图（2021/2022 销量对比，2021 柱顶带差值标记线）"""
from common import setup, save, FG

商品 = ["口红", "面膜", "隔离", "防晒", "精华"]
销量21 = [3568, 4135, 4436, 4106, 4936]
销量22 = [2569, 3241, 2965, 3209, 3541]

fig, ax = setup()
x = list(range(len(商品)))
w = 0.36
ax.bar([xi - w / 2 - 0.03 for xi in x], 销量21, width=w,
       color="#0070C0", zorder=3)
ax.bar([xi + w / 2 + 0.03 for xi in x], 销量22, width=w,
       color="#82ADD7", zorder=3)
for xi, v in zip(x, 销量21):
    # 柱顶的蓝色短横线标记（原图为图片标记）
    ax.plot([xi - w / 2 - 0.06, xi + w / 2 - 0.0], [v, v],
            color="#0070C0", linewidth=4, solid_capstyle="butt", zorder=4)
    ax.text(xi - w / 2 - 0.03, v + 90, f"{v}", ha="center", va="bottom",
            color=FG, fontsize=11, zorder=5)
for xi, v in zip(x, 销量22):
    ax.text(xi + w / 2 + 0.03, v - 90, f"{v}", ha="center", va="top",
            color=FG, fontsize=11, zorder=5)

ax.set_xticks(x)
ax.set_xticklabels(商品, color=FG)
ax.set_ylim(0, 5700)
ax.set_yticks([])
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
# 底部图例
from matplotlib.patches import Patch
import matplotlib.lines as mlines
ax.legend(handles=[
    Patch(color="#0070C0", label="2021销量"),
    Patch(color="#82ADD7", label="2022销量"),
    mlines.Line2D([], [], color="#0070C0", linewidth=4, label="差值"),
], loc="lower center", bbox_to_anchor=(0.5, -0.14), ncol=3,
   frameon=False, labelcolor=FG, fontsize=11)
save(fig, "09_对比柱形图")
