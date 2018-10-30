import socket

target_host = "httpbin.org"
target_port = 80

GET  = "GET / HTTP/1.1\r\n"
HOST = "Host: " + target_host + "\r\n"
USER_AGENT = "User-Agent: " + "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0\r\n"
message = GET + HOST + USER_AGENT + "\r\n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((target_host, target_port))
s.send(message.encode('utf-8'))

resp = s.recv(1024)
print(resp)

s.close()


# The AF_INET parameter is saying we are going to use IPv4
# SOCK_STREAM is saying we are going to use TCP

# Assumptions we make:
# 1. Our connection will always succeed
# 2. The server is expecting us to send data first
# 3. The server will always send us data back
