import bluetooth

server_sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
port = 1	#设置端口号
server_sock.bind(("", port))	#绑定地址和端口
server_sock.listen(5)	#绑定监听，最大挂起连接数为1
if __name__ =='__main__':
    try:
        while True:
            print('正在等待接收数据。。。')
            client_sock,address=server_sock.accept()  #阻塞等待连接
            print('连接成功')
            print("Accepted connection from ", address)
            while True:
                data =client_sock.recv(1024).decode() #不断接收数据，每次接收缓冲区1024字节
                print("received [%s]" % data)
    except:
        client_sock.close()
        server_sock.close()
        print('disconnect!')