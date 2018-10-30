import requests

target_host = "http://www.httpbin.org/ip"
s = requests.session()
proxies = {
    'http' : 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'
}

resp = requests.get(target_host, proxies=proxies)
print(resp.text)
print(resp.request.headers) # user agent: python-requests{version}
