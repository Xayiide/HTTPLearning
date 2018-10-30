import socket

target_host = "127.0.0.1"
target_port = 80

GET = "GET /images/Phantom.png HTTP/1.1\r\n"
HOST = "Host: " + target_host + "\r\n"
USER_AGENT = "User-Agent: " + "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0\r\n"
message = GET + HOST + USER_AGENT + "\r\n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((target_host, target_port))
s.send(message.encode('utf-8'))


resp = s.recv(8192) # La imagen es grande, mejor poner un buen size

print(resp[:400]) # Esta en byte
# En resp estará la respuesta del servidor + los byt    es de la imagen
# El magicnumber de png es: 89 50 4e 47 0d 0a 1a 0a == 89504e470d0a1a0a
# Podemos leer hasta encontrar eso y luego borrar todo lo anterior

resp2 = resp.decode('utf-8')
print(resp2[:400])

magicnumber = "89504e470d0a1a0a"

# Es un poco movida coger sólo los bytes de la imagen para guardarla

s.close()
