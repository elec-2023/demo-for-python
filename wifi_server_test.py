import socket
import subprocess
import time
import threading

a=0
def thread_wait():
    global a
    a+=1
    print(f'this is the {a}-th input')
    time.sleep(1)
    print(f'{a}-th input end')
    
    
def start_server():
    # 本地IP和端口
    host = '192.168.12.1'
    port = 12345

    # 创建socket对象
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定IP和端口
    server_socket.bind((host, port))

    # 监听客户端连接
    server_socket.listen(1)
    print(f"等待客户端连接...")

    while True:
        # 接受客户端连接
        client_socket, client_address = server_socket.accept()
        print(f"连接来自：{client_address}")

        # 处理客户端发送的命令
        while True:
            try:
                command = client_socket.recv(1024).decode()
                if not command:
                    break
                threading.Thread(target=thread_wait).start()
                # 执行命令并获取输出
                output = subprocess.getoutput(command)

                # 将命令输出发送给客户端
                client_socket.sendall(output.encode())

            except Exception as e:
                print(f"发生错误：{e}")
                break

        # 关闭当前客户端连接
        client_socket.close()
        print(f"连接关闭")

if __name__ == "__main__":
    start_server()
