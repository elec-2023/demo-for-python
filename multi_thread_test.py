import threading
import time

running = True
serial_signal = "1"  # 初始串口信号为1
kill =4
def son01():
    global kill
    while kill!=1:
        print(f'I am son01,kill={kill}')
        time.sleep(5)
def son02():
    global kill
    while kill!=2:
        print(f'I am son02,kill={kill}')
        time.sleep(3)
def son03():
    global kill
    while kill!=3:
        print(f'I am son03,kill={kill}')
        time.sleep(2)
def father():
    global kill
    while 1:
        kill=int(input())
son01thread=threading.Thread(target=son01)
son02thread=threading.Thread(target=son02)
son03thread=threading.Thread(target=son03)
fatherthread=threading.Thread(target=father)

son01thread.start()
son02thread.start()
son03thread.start()
fatherthread.start()