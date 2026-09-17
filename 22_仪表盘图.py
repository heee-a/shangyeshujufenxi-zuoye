# -*- coding: utf-8 -*-
"""图22：仪表盘图（270° 刻度盘：蓝底、彩色刻度段、白色指针）"""
import numpy as np
from matplotlib.patches import Wedge
from common import setup, save, FG

E_START = 225                            # Excel firstSliceAng（12 点方向顺时针）
指针数值 = 76
刻度 = list(range(50, 151, 10))          # 50..150

fig, ax = setup(7.0, 6.6, margins=(0.04, 0.06, 0.96, 0.92))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect("equal")
ax.axis("off")

cx, cy = 0.5, 0.52
R_out = 0.40
RW = 0.065
R_hole = R_out - RW                     # 孔半径（指针/标签区）

def ew(deg):
    """Excel 顺时针角（自12点）→ matplotlib 角度"""
    return (90 - deg) % 360

# 底层蓝色整环（360°）
ax.add_patch(Wedge((cx, cy), R_out, theta1=0, theta2=360, width=RW,
                   facecolor="#0070C0", edgecolor="none"))

# 刻度段：每段 27°，自 E_START 顺时针
# 第 1~3 段（50-80，青绿） 第 4~7 段（80-120，黄） 第 8~10 段（120-150，红）
段色 = ["#087E8B"] * 3 + ["#FFC54D"] * 4 + ["#F94C66"] * 3
for i, color in enumerate(段色):
    e0 = E_START + i * 27
    e1 = e0 + 27
    t1 = ew(e1)
    t2 = ew(e0)
    ax.add_patch(Wedge((cx, cy), R_out, theta1=t1, theta2=t2, width=RW,
                       facecolor=color, edgecolor="none"))

# 刻度标签（每段起点处）
for i, v in enumerate(刻度):
    ang = E_START + i * 27
    rad = np.radians(ang)
    lx = cx + (R_hole - 0.075) * np.sin(rad)
    ly = cy + (R_hole - 0.075) * np.cos(rad)
    ax.text(lx, ly, str(v), ha="center", va="center",
            color="#C9C9DD", fontsize=9)

# 指针（白色楔形，跨度 70.2°）+ 指针尖端线
指针角 = E_START + (指针数值 - 50) / 100 * 270
t1 = ew(指针角 + 70.2)
t2 = ew(指针角)
ax.add_patch(Wedge((cx, cy), R_hole, theta1=t1, theta2=t2, width=R_hole * 0.9,
                   facecolor="#E8E8F0", edgecolor="none", alpha=0.85))
ax.add_patch(Wedge((cx, cy), 0.02, theta1=0, theta2=360,
                   facecolor="#E8E8F0", edgecolor="none"))

# 中心数值
ax.text(cx, cy - 0.06, str(指针数值), ha="center", va="center",
        color=FG, fontsize=34, fontweight="bold")
ax.text(cx, cy - 0.145, "完成率(%)", ha="center", va="center",
        color="#C9C9DD", fontsize=10)
save(fig, "22_仪表盘图")
