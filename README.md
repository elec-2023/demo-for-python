# python-demo
Little modules work for electronic competitions 2023

`multi_thread_test`:针对python的多线程运行方式测试，通过static变量控制全局


`video_test`:测试摄像头是否可以使用

`gpio_test`:可以检测传入信号上升沿和下降沿的demo，demo为用于重启的程序

`serial_pot_out_in`,`serial_test_time_mv`:在树莓派上为多线程执行架构，在mv上由于不支持多线程暂未修改

使用方法：

1. 基础使用：

   1. openmv向树莓派发送信息：

      ```python
      import time,pyb
      from pyb import Pin, Timer,UART,LED
      uart=UART(3,19200)
      uart.write("test_function;input\n")
      ```

      注意！！！！输出格式为%函数名;参数%，需要注意的是为了解析统一所有以该方式调用的函数应接受1个str类型输入

   2. 树莓派注册信息监听：

      ```python
      def test_function(str):
      ```

      和正常函数一样，但参数必须为字符串类型

   3. 树莓派发送信息：

      ```python
      send_to_mv('inputinputinputinputinputinputinput')
      ```

   4. openmv监听信息

      ```python
      import time,pyb
      
      from pyb import Pin, Timer,UART,LED
      uart=UART(3,19200)
      while 1:
          data = uart.read()
          if data is not None:
              print(data.decode())
              break
      ```



