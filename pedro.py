from socket import *

serverName = '10.10.248.177' # Completar com o IP do servidor 
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

print("Conectado ao servidor. Digite uma letra por vez (ou 'D' para sair):")

while True:
    letra = input("Enviar caractere: ")
    if len(letra) > 0:
        clientSocket.send(letra[0].encode())
        
        if letra[0] == 'D':
            break
            
        resposta = clientSocket.recv(1024).decode()
        print(f"Servidor: {resposta}")

clientSocket.close()
print("Conexão encerrada.")