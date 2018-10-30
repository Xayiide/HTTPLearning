import socket
import socks

target_host = "httpbin.org"
target_port = 80

GET  = "GET /ip HTTP/1.1\r\n"
HOST = "Host: " + target_host + "\r\n"
USER_AGENT = "User-Agent: " + "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0\r\n"
message = GET + HOST + USER_AGENT + "\r\n"

socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050, True)
s = socks.socksocket()
s.connect((target_host, target_port))
s.send(message.encode('utf-8'))

resp = s.recv(4096)
aux = resp.decode('utf-8')
print(aux)
