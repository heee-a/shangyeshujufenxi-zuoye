# -*- coding: utf-8 -*-
"""图8：数值百分比（销量条形 + 右侧固定红色标签区显示同比）"""
from common import setup, save, FG

区域 = ["华北", "华南", "东北", "西北", "西南", "华东"]
销量 = [4321, 1946, 1536, 1872, 1369, 2109]
占位1 = [0, 2375, 2785, 2449, 2952, 2212]
同比 = [-0.136, -0.208, -0.093, -0.159, -0.179, -0.058]

总长 = 5401.25
标签区宽 = 1080.25

fig, ax = setup()
y = list(range(len(区域)))[::-1]
h = 0.7
for yi, v, p1 in zip(y, 销量, 占位1):
    ax.barh(yi, v, height=h, color="#09387E", zorder=3)         # 销量（深蓝）
    ax.barh(yi, p1, left=v, height=h, color="#82ADD7", zorder=3)  # 占位（浅蓝）
# 右侧红色标签区（所有行位置一致）
for yi in y:
    ax.barh(yi, 标签区宽, left=总长 - 标签区宽, height=h,
            color="#9B3D4F", zorder=4)
for yi, v in zip(y, 销量):
    ax.text(v + 90, yi, f"{v}", va="center", ha="left",
            color=FG, fontsize=11, zorder=5)
for yi, t in zip(y, 同比):
    ax.text(总长 - 标签区宽 / 2, yi, f"{t:.1%}", va="center", ha="center",
            color=FG, fontsize=11, zorder=6)

ax.set_xlim(0, 总长 + 150)
ax.set_yticks(y)
ax.set_yticklabels(区域[::-1], color=FG)
ax.set_xticks([])
ax.spines["left"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_visible(False)
save(fig, "08_数值百分比")
