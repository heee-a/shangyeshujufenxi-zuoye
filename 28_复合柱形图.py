# -*- coding: utf-8 -*-
"""图28：复合柱形图（季度宽柱 + 月度窄柱，按季度着色）"""
from common import setup, save, FG

月份 = ["1月", "2月", "3月", "4月", "5月", "6月",
        "7月", "8月", "9月", "10月", "11月", "12月"]
月度 = [2354, 1902, 3524, 2698, 2896, 2563, 3156, 2896, 3621, 2635, 2963, 2789]
季度 = [7780, 8157, 9673, 8387]
季色 = ["#4A5BD1", "#FC6C0F", "#F6A50B", "#A2417B"]

fig, ax = setup(8.4, 6.2)
x = list(range(len(月份)))
# 季度宽柱（每季 3 个月）
for q in range(4):
    xi = q * 3 + 1
    ax.bar(xi, 季度[q], width=2.75, color=季色[q], alpha=0.55, zorder=2)
# 月度窄柱
for i, v in enumerate(月度):
    ax.bar(i, v, width=0.55, color=季色[i // 3], zorder=3)
    ax.text(i, v + 130, f"{v}", ha="center", va="bottom",
            color=FG, fontsize=9, zorder=4)

ax.set_xticks(x)
ax.set_xticklabels(月份, color=FG)
ax.set_ylim(0, 12000)
ax.set_yticks([0, 4000, 8000, 12000])
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
save(fig, "28_复合柱形图")
