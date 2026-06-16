# TCPServer.py
# Adaptado de Kurose & Ross, "Redes de Computadores e a Internet", Cap. 2.
# Servidor TCP que recebe uma mensagem, converte para maiusculas e devolve.

from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive")

while True:
    connectionSocket, addr = serverSocket.accept()

    while True:
        # strip para limpar o dado obtido
        sentence = connectionSocket.recv(1024).decode().strip()
        print('From client:', sentence)
        connectionSocket.send(sentence.encode())
        if(sentence == 'X'):
            break;

    print('Conexão encerrada')
    connectionSocket.close()