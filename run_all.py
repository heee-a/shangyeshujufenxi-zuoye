# -*- coding: utf-8 -*-
"""一键重绘全部图表。

用法：
    python run_all.py            # 按编号顺序重绘 01 ~ 30 全部图表
    python run_all.py 03 15      # 只重绘指定编号（可传多个）

每个脚本独立运行，单张失败不影响其余图表；全部产物写入 outputs/。
"""
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main() -> int:
    wanted = {a.zfill(2) for a in sys.argv[1:]}
    scripts = sorted(ROOT.glob("[0-3][0-9]_*.py"))
    if wanted:
        scripts = [s for s in scripts if s.name[:2] in wanted]
    if not scripts:
        print("未找到匹配的图表脚本")
        return 1

    print(f"共 {len(scripts)} 个图表脚本待重绘\n")
    failed = []
    t0 = time.time()
    for i, s in enumerate(scripts, 1):
        print(f"[{i}/{len(scripts)}] {s.name}")
        r = subprocess.run([sys.executable, s.name], cwd=ROOT,
                           capture_output=True, text=True)
        if r.returncode != 0:
            failed.append(s.name)
            print(r.stderr.strip()[-800:])

    print(f"\n完成 {len(scripts) - len(failed)}/{len(scripts)}，"
          f"耗时 {time.time() - t0:.1f}s")
    if failed:
        print("失败：{}".format("、".join(failed)))
        return 1
    print("全部图表已导出至 outputs/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
