# 我的第一个 Python 程序
# 日期：2026-11-24
# 目的：确认 Python 能跑，并看清它用的是哪个解释器

import sys

name = "JT"
print(f"你好，{name}！")
print("如果你看到这一行，说明 Python 已经能正常工作了。")
print("-" * 40)

# 顺便证明它能干活
total = sum(range(1, 101))
print(f"1 到 100 相加 = {total}")

# 这三个信息以后排错时会经常用到
print("-" * 40)
print(f"Python 版本：{sys.version.split()[0]}")
print(f"解释器路径：{sys.executable}")
