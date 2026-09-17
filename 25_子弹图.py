# -*- coding: utf-8 -*-
"""图25：子弹图（定性分段底色 + 实际柱 + 目标刻度线）"""
from common import setup, save, FG

商品 = ["口红", "面膜", "隔离", "防晒", "精华", "面霜"]
实际 = [653, 523, 648, 856, 714, 785]
目标 = [700, 500, 600, 900, 600, 600]

fig, ax = setup()
x = list(range(len(商品)))
# 定性分段（及格 0-600 浅蓝 / 良好 600-800 亮蓝 / 优秀 800-1000 深蓝）
ax.bar(x, [600] * 6, width=0.7, color="#82ADD7", zorder=2)
ax.bar(x, [200] * 6, width=0.7, bottom=[600] * 6, color="#00B0F0", zorder=2)
ax.bar(x, [200] * 6, width=0.7, bottom=[800] * 6, color="#0070C0", zorder=2)
# 实际值
ax.bar(x, 实际, width=0.34, color="#0E5DFF", zorder=3)
for xi, v in zip(x, 实际):
    ax.text(xi, v + 45, f"{v}", ha="center", va="bottom",
            color=FG, fontsize=11, zorder=4)
# 目标刻度线（柱顶横线标记）
for xi, t in zip(x, 目标):
    ax.plot([xi - 0.17, xi + 0.17], [t, t], color="#F0F0F5",
            linewidth=3, zorder=5)

ax.set_xticks(x)
ax.set_xticklabels(商品, color=FG)
ax.set_ylim(0, 1200)
ax.set_yticks([])
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
# 底部图例
from matplotlib.patches import Patch
ax.legend(handles=[
    Patch(color="#0E5DFF", label="实际"),
    Patch(color="#82ADD7", label="及格"),
    Patch(color="#00B0F0", label="良好"),
    Patch(color="#0070C0", label="优秀"),
], loc="lower center", bbox_to_anchor=(0.5, -0.16), ncol=4,
   frameon=False, labelcolor=FG, fontsize=10)
save(fig, "25_子弹图")
