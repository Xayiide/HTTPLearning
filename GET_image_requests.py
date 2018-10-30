import requests

target_host = "http://127.0.0.1:80/images/Phantom.png"
target_port = 80

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
          }
resp = requests.get(target_host, headers=headers)

with open('phantom.png', 'wb') as f:
    f.write(resp.content)

# Con requests es muy sencillo coger solamente los bytes 
