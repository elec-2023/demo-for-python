import cv2, os
import sys
import RPi.GPIO as GPIO

button_reset = 4
# 设置GPIO模式为BCM
GPIO.setmode(GPIO.BCM)
# 配置按钮引脚为输入模式，使用内部上拉电阻
GPIO.setup(button_reset, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def restart_program(channel):
    """重新启动当前程序"""
    # 在此处添加任何清理操作
    python = sys.executable
    os.execl(python, python, *sys.argv)


# 注册按钮按下事件的回调函数
GPIO.add_event_detect(button_reset, GPIO.FALLING, callback=restart_program, bouncetime=200)