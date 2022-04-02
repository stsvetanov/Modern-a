# https://www.geeksforgeeks.org/socket-programming-python/

# first of all import the socket library
import socket

# next create a socket object
s = socket.socket()
print("Socket successfully created")

# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12345

# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))

print(f"Socket binded to port {port}")

# put the socket into listening mode
s.listen(5)
print("Socket is listening")

# a forever loop until we interrupt it or
# an error occurs
while True:
    # Establish connection with client.
    connection, address = s.accept()
    print(f'Got connection from address {address}')

    # send a thank you message to the client.
    connection.send('Thank you for connecting'.encode())
    data = connection.recv(10)
    print(data.decode())

    # Close the connection with the client
    connection.close()
