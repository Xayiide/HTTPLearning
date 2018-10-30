import requests

target_host = "https://httpbin.org/post"

resp = requests.post(target_host)

print(resp.text)
