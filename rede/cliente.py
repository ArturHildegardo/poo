import socket

ip = "localhost"
port = 8000
addr = ((ip,port))
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(addr)

mensagem = None

while mensagem != "sair":
	mensagem = input("Digite uma mensagem para o servidor: ")
	if mensagem == 'sair':
		print ('fim da Conexão')
		client_socket.close()
	else:
		client_socket.send(mensagem.encode())
		print("Mensagem enviada!")
		print("servidor: {}".format(client_socket.recv(1024).decode()))
