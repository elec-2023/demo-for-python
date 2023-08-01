import serial,time,threading

ser = serial.Serial('/dev/ttyS0', 19200)

kill=0
info=[]


def test_function(str):
    print('(test_function)I am test function')
    print(f'(test_function)I received {str}')
    time.sleep(2)
    print('(test_function)I sleep 2s and wake up again')
    send_to_mv('(test_function)test function will stop soon')
    print('(test_function)I will stop now')


def send_to_mv(data):
    ser.write(data.encode())


while 1:
    print('(main thread)Start listening to serial port at /dev/ttyS0')
    data = ser.readline()
    print(data.decode().strip())
    try:
        input=data.decode().strip().split(';')
        target_function = globals()[input[0]]
        print(input)
        if callable(target_function):
            # Execute the function in a separate thread
            thread = threading.Thread(target=target_function,args=("aa",))
            thread.start()
            print('2')
        else:
            print("Error: The provided input is not a callable function.")
    except Exception as e:
        print(e)
        print('failed')
    print('1')
    send_to_mv('1234')
