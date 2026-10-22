# -*- coding: utf-8 -*-
"""图30：对比滑珠图（2022/2021 双轨滑珠对比）

每个区域占一组上下双轨：上轨为 2022 年（蓝），下轨为 2021 年（灰蓝），
滑珠落在完成率处，数值标注在滑珠右侧，避免两年数值接近时滑珠互相遮挡。
"""
from matplotlib.patches import Circle
from matplotlib.lines import Line2D
from common import setup, save, FG

区域 = ["华东", "西北", "东北", "华北", "华南"]
年22 = [0.35, 0.51, 0.62, 0.74, 0.86]   # 2022 年完成率（蓝）
年21 = [0.45, 0.39, 0.53, 0.69, 0.92]   # 2021 年完成率（灰蓝）

fig, ax = setup()
y = [3, 5, 7, 9, 11]                    # 每个区域的中心组
off = 0.32                              # 上/下轨偏移
track_h = 0.30                          # 轨道高度
r = 0.12                                # 滑珠半径

for yi, v22, v21 in zip(y, 年22, 年21):
    for yv, v, c, ec in [(yi + off, v22, "#0070C0", "#BFE3FF"),
                         (yi - off, v21, "#8A8FA8", "#D8D8E0")]:
        # 轨道：全长浅深灰 + 完成部分着色
        ax.barh(yv, 1.0, height=track_h, color="#2E3560", zorder=2)
        ax.barh(yv, v, height=track_h, color=c, zorder=3)
        # 滑珠 + 右侧数值标签
        ax.add_patch(Circle((v, yv), r, facecolor=c, edgecolor=ec,
                            linewidth=1.5, zorder=4))
        ax.text(v + r + 0.025, yv, f"{v:.2f}", ha="left", va="center",
                color=FG, fontsize=10, zorder=5)

ax.set_yticks(y)
ax.set_yticklabels(区域, color=FG, fontsize=12)
ax.set_ylim(0.8, 12.6)
ax.set_xlim(0, 1.24)
ax.set_xticks([])
for s in ax.spines.values():
    s.set_visible(False)
ax.legend(handles=[
    Line2D([0], [0], marker="o", color="none", markerfacecolor="#0070C0",
           markeredgecolor="#BFE3FF", markersize=11, label="2022年"),
    Line2D([0], [0], marker="o", color="none", markerfacecolor="#8A8FA8",
           markeredgecolor="#D8D8E0", markersize=11, label="2021年"),
], loc="lower right", frameon=False, fontsize=11, labelcolor=FG, ncol=2)
save(fig, "30_对比滑珠图")
