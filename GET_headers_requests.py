import requests

target_host = "http://127.0.0.1/php-show-data.php"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
          }
resp = requests.get(target_host, headers=headers)
print(resp.text, "\n\n") #
