# -*- coding: utf-8 -*-
"""图29：滑珠图（横向条形 + 端点滑珠）"""
from matplotlib.patches import Circle
from common import setup, save, FG

区域 = ["华东", "西北", "东北", "华北", "华南"]
完成率 = [0.35, 0.51, 0.62, 0.74, 0.86]

fig, ax = setup()
y = [1, 3, 5, 7, 9]                     # 原图为辅助轴等距放置
h = 0.9
for yi, v in zip(y, 完成率):
    # 完成部分（浅蓝）+ 未完成占位（橙）
    ax.barh(yi, v, height=h, color="#5B9BD5", zorder=2)
    ax.barh(yi, 1 - v, left=v, height=h, color="#ED7D31", zorder=2)
    # 滑珠
    ax.add_patch(Circle((v, yi), 0.24, facecolor="#0070C0",
                        edgecolor="#BFE3FF", linewidth=1.5, zorder=4))
    ax.text(v, yi, f"{v:.2f}", ha="center", va="center",
            color=FG, fontsize=10, zorder=5)

ax.set_yticks(y)
ax.set_yticklabels(区域, color=FG)
ax.set_ylim(0.2, 9.8)
ax.set_xlim(0, 1.06)
ax.set_xticks([])
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_visible(False)
save(fig, "29_滑珠图")
