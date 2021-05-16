import socket
host = "localhost"
port = 8000
addr = (host, port)
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv_socket.bind(addr)
serv_socket.listen(10)
print("aguardando conexao")
con, client = serv_socket.accept()
print("Conectando")
print("Aguardando mensagem")

enviar = None
while (enviar != "sair"):
	recebe = con.recv(1024)
	if (recebe.decode() != 'sair'):
		print("Cliente: " + recebe.decode())
		enviar = input("Digite uma mensagem para enviar ao cliente: ")
		con.send(enviar.encode())
	else:
		serve_socket.close()
