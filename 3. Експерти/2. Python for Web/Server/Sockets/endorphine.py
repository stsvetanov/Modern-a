import socket
import time

s = socket.socket()
print("Socket successfully created")

port = 6666

s.bind(('', port))
print(f"Socket binded to port {port}")

s.listen(5)
print("Socket is listening")

while True:
    connection, address = s.accept()
    print(f'Got connection from address {address}')

    # connection.send('#RHOR0000\r'.encode())
    # time.sleep(2)
    # data = connection.recv(4)
    # print(data.decode())
    #
    # time.sleep(3)

    # connection.send('#WHOR0004\r'.encode())
    # time.sleep(2)
    # data = connection.recv(4)
    # print(data.decode())
    #
    # time.sleep(3)

    connection.send('#RHOR0000\r'.encode())
    time.sleep(1)
    data = connection.recv(4)
    print(data.decode())

    connection.close()
