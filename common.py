# -*- coding: utf-8 -*-
"""公共绘图基座：统一画布、配色、渐变柱形与导出。

设计体系（深色 PPT 风，复刻自《第二章 图表(前15).xlsx》）：
    BG   #1A1E43  画布背景（深海军蓝）
    FG   #E8E8F0  主文字 / 刻度文字
    SUB  #8888AA  次级说明文字
    GRID #2E3560  网格线与坐标轴
主色板：#0070C0（主蓝）#00B0F0（亮蓝）#37A2DA #11A7AD（青）#F5C353（黄）#E74E69（玫红）#7030A0（紫）

对外接口（供 01~30 各图脚本引用）：
    setup(figsize_w, figsize_h, margins) -> (fig, ax)   深色画布 + 统一刻度样式
    save(fig, name)                   -> Path           导出 200dpi PNG 到 outputs/
    gradient_bar(ax, x, y, w, h, c1, c2, rounded=False) 底深顶浅的垂直渐变柱
    BG / FG / SUB / GRID / OUTPUT_DIR
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # 无显示环境，必须在 pyplot 导入前设置

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import PathPatch, Rectangle
from matplotlib.path import Path as MplPath

# ---------------------------------------------------------------- 设计体系
BG = "#1A1E43"      # 画布背景（深海军蓝）
FG = "#E8E8F0"      # 主文字 / 刻度文字
SUB = "#8888AA"     # 次级说明文字
GRID = "#2E3560"    # 网格线与坐标轴

OUTPUT_DIR = Path(__file__).resolve().parent / "outputs"
DPI = 200


def _pick_cjk_font() -> str:
    """按可用性挑选中文字体，缺省回退 SimHei，保证跨平台不出方框。"""
    preferred = [
        "Microsoft YaHei", "PingFang SC", "Noto Sans CJK SC",
        "Source Han Sans SC", "SimHei", "WenQuanYi Micro Hei",
    ]
    available = {f.name for f in font_manager.fontManager.ttflist}
    for name in preferred:
        if name in available:
            return name
    return "sans-serif"


def _apply_style() -> None:
    """全局 rcParams：中文字体 + 负号修复 + 深色刻度。"""
    plt.rcParams["font.family"] = "sans-serif"
    plt.rcParams["font.sans-serif"] = [_pick_cjk_font()] + [
        "DejaVu Sans",
    ]
    plt.rcParams["axes.unicode_minus"] = False


_apply_style()


# ---------------------------------------------------------------- 画布
def setup(figsize_w: float = 8.8, figsize_h: float = 6.2,
          margins: tuple = (0.08, 0.10, 0.96, 0.94)):
    """创建深色画布。

    Parameters
    ----------
    figsize_w, figsize_h : 画布尺寸（英寸）
    margins : (left, bottom, right, top) 子图边距，直接透传给 subplots_adjust

    Returns
    -------
    (fig, ax) : 背景已设为 BG 的 Figure 与单一 Axes
    """
    fig = plt.figure(figsize=(figsize_w, figsize_h), facecolor=BG)
    ax = fig.add_subplot(111)
    fig.subplots_adjust(*margins)

    ax.set_facecolor(BG)
    ax.tick_params(colors=FG, labelsize=11, length=4, color=GRID)
    for side in ("left", "bottom", "top", "right"):
        ax.spines[side].set_color(GRID)
        ax.spines[side].set_linewidth(0.8)
    return fig, ax


# ---------------------------------------------------------------- 导出
def save(fig, name: str) -> Path:
    """按 200dpi 导出 PNG 到 outputs/，并释放画布。"""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUTPUT_DIR / f"{name}.png"
    fig.savefig(path, dpi=DPI, facecolor=BG, bbox_inches=None)
    plt.close(fig)
    print(f"已导出 {path.name}")
    return path


# ---------------------------------------------------------------- 渐变柱
def _rounded_top_path(x: float, y: float, w: float, h: float, r: float) -> MplPath:
    """仅顶部两角为圆角的矩形路径（r 自动收敛到合法范围）。"""
    r = max(0.0, min(r, w / 2.0, h))
    verts = [
        (x, y),                       # 左下
        (x, y + h - r),               # 左圆角起点
        (x, y + h), (x + r, y + h),   # 左上圆角（二次贝塞尔）
        (x + w - r, y + h),           # 顶边
        (x + w, y + h), (x + w, y + h - r),  # 右上圆角
        (x + w, y),                   # 右下
        (x, y),                       # 闭合
    ]
    codes = [
        MplPath.MOVETO,
        MplPath.LINETO,
        MplPath.CURVE3, MplPath.CURVE3,
        MplPath.LINETO,
        MplPath.CURVE3, MplPath.CURVE3,
        MplPath.LINETO,
        MplPath.CLOSEPOLY,
    ]
    return MplPath(verts, codes)


def gradient_bar(ax, x: float, y: float, w: float, h: float,
                 c_bottom: str, c_top: str, rounded: bool = False,
                 zorder: int = 2):
    """绘制底深顶浅的垂直渐变柱。

    Parameters
    ----------
    ax        : 目标 Axes
    x, y      : 柱体左下角（数据坐标）
    w, h      : 柱体宽与高
    c_bottom  : 底部颜色（深）
    c_top     : 顶部颜色（浅）
    rounded   : True 时顶部两角圆角（圆角半径 = w / 2）
    zorder    : 绘制层级，默认位于文字之下

    Notes
    -----
    实现为 imshow 线性渐变 + Path 裁剪；数据坐标随轴缩放自动适配，
    因此调用之后再 set_ylim / set_aspect 均不影响渐变填充。
    """
    if h <= 0 or w <= 0:
        raise ValueError(f"gradient_bar 尺寸必须为正：w={w}, h={h}")

    cmap = LinearSegmentedColormap.from_list("gradient_bar", [c_bottom, c_top])
    grad = np.linspace(0.0, 1.0, 256).reshape(-1, 1)
    im = ax.imshow(grad, extent=[x, x + w, y, y + h], aspect="auto",
                   cmap=cmap, origin="lower", zorder=zorder,
                   interpolation="bilinear")

    if rounded:
        clip = PathPatch(_rounded_top_path(x, y, w, h, w / 2.0),
                         facecolor="none", edgecolor="none", zorder=zorder)
    else:
        clip = Rectangle((x, y), w, h,
                         facecolor="none", edgecolor="none", zorder=zorder)
    ax.add_patch(clip)
    im.set_clip_path(clip)
    return im
