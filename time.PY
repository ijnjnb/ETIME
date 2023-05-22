# 导入time模块
import time

# 定义工作时间和休息时间的分钟数
work_minutes = 25
break_minutes = 5

# 定义一个函数，用于显示倒计时
def countdown(minutes):
  # 将分钟转换为秒数
  seconds = minutes * 60
  # 循环直到秒数为0
  while seconds > 0:
    # 打印当前的分钟和秒数，格式为mm:ss
    print(f"{seconds // 60:02d}:{seconds % 60:02d}", end="\r")
    # 每隔一秒减少一秒
    time.sleep(1)
    seconds -= 1
  # 打印换行符
  print()

# 开始专注时钟的循环
while True:
  # 打印开始工作的提示
  print("开始工作！")
  # 调用倒计时函数，传入工作时间
  countdown(work_minutes)
  # 打印开始休息的提示
  print("开始休息！")
  # 调用倒计时函数，传入休息时间
  countdown(break_minutes)
