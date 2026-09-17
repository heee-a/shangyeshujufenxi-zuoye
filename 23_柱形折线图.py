# -*- coding: utf-8 -*-
"""图23：柱形折线图（销售量柱形 + 同比折线，双轴）"""
from common import setup, save, FG

年份 = ["2017", "2018", "2019", "2020", "2021", "2022"]
销售量 = [1603, 2106, 2406, 3265, 3721, 3921]
同比 = [0.27, 0.3138, 0.1425, 0.3570, 0.1397, 0.0537]

fig, ax = setup()
x = list(range(len(年份)))
ax.bar(x, 销售量, width=0.42, color="#0070C0", zorder=3)
for xi, v in zip(x, 销售量):
    ax.text(xi, v + 130, f"{v}", ha="center", va="bottom",
            color=FG, fontsize=11, zorder=4)

ax2 = ax.twinx()
ax2.plot(x, 同比, color="#E74E69", linewidth=1.5, marker="o",
         markersize=5, markerfacecolor="#E74E69", markeredgecolor="#FFD0D8",
         zorder=5)
for xi, v in zip(x, 同比):
    ax2.text(xi, v + 0.045, f"{v:.2f}", ha="center", va="bottom",
             color="#FF8A9A", fontsize=10, zorder=6)

ax.set_xticks(x)
ax.set_xticklabels(年份, color=FG)
ax.set_ylim(0, 6000)
ax.set_yticks([0, 2000, 4000, 6000])
ax2.set_ylim(-1.2, 0.5)
ax2.set_yticks([-1.0, -0.5, 0, 0.5])
ax2.tick_params(colors="#C9C9DD")
ax2.spines["top"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax2.spines["right"].set_color("#5A5A80")

# 底部图例
from matplotlib.patches import Patch
import matplotlib.lines as mlines
ax.legend(handles=[
    Patch(color="#0070C0", label="销售量"),
    mlines.Line2D([], [], color="#E74E69", marker="o", label="同比"),
], loc="lower center", bbox_to_anchor=(0.5, -0.15), ncol=2,
   frameon=False, labelcolor=FG, fontsize=11)
save(fig, "23_柱形折线图")
