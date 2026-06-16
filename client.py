# TCPClient.py
# Adaptado de Kurose & Ross, "Redes de Computadores e a Internet", Cap. 2.
# Cliente TCP que envia uma frase e recebe-a de volta em maiusculas.
#
# Antes de executar, ajuste serverName para o IP ou hostname do servidor.

from socket import *

serverName = '192.168.1.1'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while True:
    sentence = input('Input sentence: ')
    clientSocket.send(sentence.encode())

    if sentence == 'X':
        break;
    
    modifiedSentence = clientSocket.recv(1024)
    print('From Server:', modifiedSentence.decode())

print('Conexão encerrada')
clientSocket.close()