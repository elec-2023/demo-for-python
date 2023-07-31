import socket

def send_command_to_server(host, port):
    try:
        # 创建socket对象
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 连接到服务端
        client_socket.connect((host, port))
        print(f"成功连接到服务端 {host}:{port}")

        while True:
            # 输入命令
            command = input("请输入要执行的命令（输入 'exit' 退出）：")

            if command.lower() == 'exit':
                break

            # 发送命令到服务端
            client_socket.sendall(command.encode())

            # 接收服务端返回的结果
            result = client_socket.recv(4096).decode()

            # 输出结果
            print("执行结果：")
            print(result)

    except Exception as e:
        print(f"连接发生错误：{e}")

    finally:
        # 关闭客户端socket
        client_socket.close()
        print("客户端已关闭")

if __name__ == "__main__":
    # 服务端的IP和端口
    server_host = '192.168.12.1'
    server_port = 12345

    send_command_to_server(server_host, server_port)
