# -*- coding: utf-8 -*-
"""图10：甘特图（项目进度，横轴为日期，柱中显示完成度）"""
from datetime import datetime, timedelta
from common import setup, save, FG

项目 = ["制定计划", "方案设计", "资源调配", "第一阶段", "第二阶段", "第三阶段", "项目总结"]
开始 = ["2022-03-01", "2022-03-13", "2022-03-22", "2022-04-02",
        "2022-04-16", "2022-05-11", "2022-05-26"]
天数 = [11, 8, 10, 13, 24, 14, 7]
完成度 = [0.51, 0.32, 0.21, 0.85, 0.36, 0.68, 0.68]

fig, ax = setup(8.86, 6.2)
y = list(range(len(项目)))[::-1]
h = 0.62
for yi, s, d, c in zip(y, 开始, 天数, 完成度):
    s0 = datetime.strptime(s, "%Y-%m-%d")
    x0 = (s0 - datetime(1899, 12, 30)).days      # Excel 日期序列
    ax.barh(yi, d, left=x0, height=h, color="#0070C0", zorder=3)
    ax.text(x0 + d / 2, yi, f"{c:.0%}", va="center", ha="center",
            color=FG, fontsize=11, zorder=4)

ax.set_yticks(y)
ax.set_yticklabels(项目[::-1], color=FG)
ax.set_ylim(-0.8, len(项目) - 0.2)
# 日期横轴
d0 = datetime(2022, 3, 1)
d1 = datetime(2022, 6, 15)
x0 = (d0 - datetime(1899, 12, 30)).days
x1 = (d1 - datetime(1899, 12, 30)).days
ax.set_xlim(x0 - 2, x1 + 2)
ticks = [d0 + timedelta(days=i) for i in range(0, (d1 - d0).days + 1, 15)]
ax.set_xticks([(t - datetime(1899, 12, 30)).days for t in ticks])
ax.set_xticklabels([t.strftime("%m/%d") for t in ticks], color=FG)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
save(fig, "10_甘特图")
