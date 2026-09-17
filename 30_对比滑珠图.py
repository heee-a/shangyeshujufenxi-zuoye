# -*- coding: utf-8 -*-
"""图30：对比滑珠图（2022/2021 两组滑珠对比）"""
from matplotlib.patches import Circle
from common import setup, save, FG

区域 = ["华东", "西北", "东北", "华北", "华南"]
年22 = [0.35, 0.51, 0.62, 0.74, 0.86]
年21 = [0.45, 0.39, 0.53, 0.69, 0.92]

fig, ax = setup()
y = [1, 3, 5, 7, 9]
h = 0.9
for yi, v22 in zip(y, 年22):
    # 2022 完成（蓝）+ 未完成占位（白）
    ax.barh(yi, v22, height=h, color="#0070C0", zorder=2)
    ax.barh(yi, 1 - v22, left=v22, height=h, color="#E8E8F0", zorder=2)
    # 2022 滑珠（蓝）
    ax.add_patch(Circle((v22, yi), 0.22, facecolor="#0070C0",
                        edgecolor="#BFE3FF", linewidth=1.5, zorder=4))
    ax.text(v22, yi, f"{v22:.2f}", ha="center", va="center",
            color=FG, fontsize=10, zorder=5)
for yi, v21 in zip(y, 年21):
    # 2021 滑珠（灰）
    ax.add_patch(Circle((v21, yi), 0.22, facecolor="#A5A5A5",
                        edgecolor="#D8D8E0", linewidth=1.5, zorder=4))
    ax.text(v21, yi, f"{v21:.2f}", ha="center", va="center",
            color=FG, fontsize=10, zorder=5)

ax.set_yticks(y)
ax.set_yticklabels(区域, color=FG)
ax.set_ylim(0.2, 9.8)
ax.set_xlim(0, 1.06)
ax.set_xticks([])
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_visible(False)
save(fig, "30_对比滑珠图")
