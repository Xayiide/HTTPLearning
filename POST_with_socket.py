import socket

target_host = "httpbin.org"
target_port = 80

POST = "POST /post HTTP/1.1\r\n"
HOST = "Host: " + target_host + "\r\n"
USER_AGENT = "User-Agent: " + "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0\r\n"
message = POST + HOST + USER_AGENT + "\r\n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((target_host, target_port))
s.send(message.encode('utf-8'))

resp = s.recv(4096)
aux = resp.decode('utf-8')
print(aux)

s.close()
