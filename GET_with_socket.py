import socket

target_host = "httpbin.org"
target_port = 80

GET  = "GET /get HTTP/1.1\r\n"
HOST = "Host: " + target_host + "\r\n"
USER_AGENT = "User-Agent: " + "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0\r\n"
message = GET + HOST + USER_AGENT + "\r\n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((target_host, target_port))
s.send(message.encode('utf-8'))

resp = s.recv(4096)
aux = resp.decode('utf-8')
print(aux)

s.close()

"""
La respuesta es en base de los atributos (¿cabeceras?) que pones en el GET.
Nosotros al no poner cookies, no vienen cookies en la respuesta. sockets te da
mucha flexibilidad porque puedes hacerte los paquetes que quieras, pero luego
a la hora de procesar la respuesta, te la da también en binario, sin mayor trato.
Esto puede resultar tedioso. Librerías como requests te facilitan mucho todo esto,
construyéndote los paquetes por defecto y dando pie también a personalizarlo.
"""
