# -*- coding: utf-8 -*-
"""图6：蝴蝶图（左右对比的横向条形图，中间显示区域名称）"""
from common import setup, save, FG

区域 = ["华东", "西北", "东北", "华北", "华南"]
占位左 = [2238, 2132, 2027, 1922, 1215]
销量22 = [1215, 1321, 1426, 1531, 2238]   # 2022年（蓝，左）
占位中 = [1215] * 5
销量21 = [1003, 1265, 1531, 1436, 2066]   # 2021年（红，右）

fig, ax = setup()
y = list(range(len(区域)))[::-1]          # 华东在最上
bar_h = 0.62
# 左半（2022年，蓝）
ax.barh(y, 销量22, left=占位左, height=bar_h, color="#0070C0", zorder=3)
# 右半（2021年，红）
ax.barh(y, 销量21, left=[a + b for a, b in zip(占位左, 销量22)],
        height=bar_h, color="#E74E69", zorder=3)
# 标签
for yi, v, base in zip(y, 销量22, 占位左):
    ax.text(base + 40, yi, f"{v}", va="center", ha="left",
            color=FG, fontsize=11, zorder=4)
for yi, v, base in zip(y, 销量21, [a + b for a, b in zip(占位左, 销量22)]):
    ax.text(base + v - 40, yi, f"{v}", va="center", ha="right",
            color=FG, fontsize=11, zorder=4)
# 中间区域名
for yi, name in zip(y, 区域):
    ax.text(占位左[0] + 销量22[0], yi, name, va="center", ha="center",
            color=FG, fontsize=12, zorder=5)
# 年份说明
ax.text(占位左[0] + 销量22[0] - 500, len(区域) - 0.4, "2022年",
        color="#4FC3F7", fontsize=12, ha="center", va="center")
ax.text(占位左[0] + 销量22[0] + 500, len(区域) - 0.4, "2021年",
        color="#FF8A9A", fontsize=12, ha="center", va="center")

ax.set_xlim(0, 占位左[0] + 销量22[0] + 占位中[0] + max(销量21) + 300)
ax.set_ylim(-0.7, len(区域) - 0.3)
ax.set_yticks([])
ax.set_xticks([])
for s in ax.spines.values():
    s.set_visible(False)
save(fig, "06_蝴蝶图")
