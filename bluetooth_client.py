import bluetooth
import time

target_address='E4:5F:01:8F:D1:2B'	#目的蓝牙的地址
sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
port = 1
if __name__ =='__main__':
    try:
        sock.connect((target_address, port)) #连接蓝牙
        i=1
        a=1
        while True:
            sock.send(('hello!'+str(i)).encode()) #每隔三秒发送一个字符串
            print('success')
            time.sleep(1)
            print(str(i))
            i=i+a
    except Exception as e:
        print(e)
        sock.close()

