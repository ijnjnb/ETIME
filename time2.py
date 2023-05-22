# 导入time模块
import time

# 定义一个函数，用于获取用户输入的分钟数
def get_minutes(prompt):
  # 循环直到获取有效的输入
  while True:
    # 打印提示信息，获取用户输入
    input_str = input(prompt)
    # 尝试将输入转换为整数
    try:
      input_int = int(input_str)
      # 如果输入是正数，返回输入
      if input_int > 0:
        return input_int
      # 否则，打印错误信息
      else:
        print("请输入一个正整数！")
    # 如果转换失败，打印错误信息
    except ValueError:
      print("请输入一个整数！")

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

# 获取用户输入的工作时间和休息时间的分钟数
work_minutes = get_minutes("请输入工作时间的分钟数：")
break_minutes = get_minutes("请输入休息时间的分钟数：")

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
