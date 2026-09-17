# -*- coding: utf-8 -*-
"""图11：平滑折线图（销量走势，平滑曲线 + 顶点数值）"""
import numpy as np
from scipy.interpolate import make_interp_spline
from common import setup, save, FG

月份 = ["5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月", "1月", "2月", "3月"]
销量 = [146, 198, 296, 412, 506, 615, 789, 1021, 3782, 3215, 2936]

fig, ax = setup()
x = np.arange(len(月份))
xs = np.linspace(0, len(月份) - 1, 300)
ys = make_interp_spline(x, 销量, k=2)(xs)
ax.plot(xs, ys, color="#E66B4C", linewidth=1.0, zorder=3)
for xi, v in zip(x, 销量):
    ax.text(xi, v + 130, f"{v}", ha="center", va="bottom",
            color=FG, fontsize=10, zorder=4)

ax.set_xticks(x)
ax.set_xticklabels(月份, color=FG)
ax.set_ylim(0, 4000)
ax.set_yticks([0, 1000, 2000, 3000, 4000])
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
save(fig, "11_平滑折线图")
