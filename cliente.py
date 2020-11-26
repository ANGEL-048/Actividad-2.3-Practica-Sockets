import socket
#Establecemos el tipo de conexion,ip y puerto
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 9000 
# Realizamos la conexion al la IP y puerto
sock.connect(('127.0.0.1',port))
data = sock.recv(4096)
# Cerramos el socket
sock.close()
# Mostramos los datos recibidos
print(data.decode())
