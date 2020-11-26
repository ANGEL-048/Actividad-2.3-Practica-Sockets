import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 9000 
sock.bind(('127.0.0.1',port)) 
#Se manda mensaje para la espera de una conexion del cliente
print ("El servidor esta a la espera de conexiones en el puerto ", port)
sock.listen(1)
con, client_addr=sock.accept()
print("Cliente conectado")#Mensaje que verifica que el cliente se conecta
text = "Hola, soy el servidor!" 
con.send(text.encode())
con.close() # Cerramos la conexion
sock.close() # Cerramos el socket
print("Cliente desconectado")#Mensaje en donde el cliente se desconecta