# -*- coding: utf-8 -*-
"""图27：簇状柱形折线图（2022/2021 销量簇状柱 + 同比折线，双轴）"""
from common import setup, save, FG

区域 = ["华北", "华南", "东北", "西北", "西南", "华东"]
年22 = [2354, 1902, 3524, 2698, 2896, 2563]
年21 = [2021, 1563, 3213, 2531, 2631, 2361]
同比 = [0.16, 0.22, 0.10, 0.07, 0.10, 0.09]

fig, ax = setup()
x = list(range(len(区域)))
w = 0.36
ax.bar([xi - w / 2 - 0.03 for xi in x], 年22, width=w,
       color="#0070C0", zorder=3)
ax.bar([xi + w / 2 + 0.03 for xi in x], 年21, width=w,
       color="#E74E69", zorder=3)
for xi, v in zip(x, 年22):
    ax.text(xi - w / 2 - 0.03, v + 100, f"{v}", ha="center", va="bottom",
            color=FG, fontsize=10, zorder=4)
for xi, v in zip(x, 年21):
    ax.text(xi + w / 2 + 0.03, v + 100, f"{v}", ha="center", va="bottom",
            color=FG, fontsize=10, zorder=4)

ax2 = ax.twinx()
ax2.plot(x, 同比, color="#FFC000", linewidth=1.5, marker="o",
         markersize=5, markerfacecolor="#FFC000", markeredgecolor="#FFF3D0",
         zorder=5)
for xi, v in zip(x, 同比):
    ax2.text(xi, v + 0.03, f"{v:.2f}", ha="center", va="bottom",
             color="#FFC000", fontsize=10, zorder=6)

ax.set_xticks(x)
ax.set_xticklabels(区域, color=FG)
ax.set_ylim(0, 5000)
ax.set_yticks([0, 2000, 4000])
ax2.set_ylim(-1.1, 0.5)
ax2.set_yticks([-1.0, -0.5, 0, 0.5])
ax2.tick_params(colors="#C9C9DD")
ax.spines["top"].set_visible(False)
ax2.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax2.spines["right"].set_color("#5A5A80")
save(fig, "27_簇状柱形折线图")
