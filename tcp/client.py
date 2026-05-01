import socket

def connect_server(host: str, port: int):
    cliente_socket =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    cliente_socket.connect((host,port))

    name = input('Type your name: ')
    cliente_socket.send(name.encode('utf-8'))

    while True:
        message = input('Type your message: ')
        cliente_socket.send(message.encode('utf-8'))


if __name__=='__main__':

    HOST = '192.168.18.17'
    PORT = 8000

    connect_server(HOST,PORT)
