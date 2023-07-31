import time,pyb

from pyb import Pin, Timer,UART,LED
uart=UART(3,19200)
print(pyb.millis())
uart.write("test_function\n")
print('send')
while 1:
    data = uart.read()
    if data is not None:
        print(data.decode())
