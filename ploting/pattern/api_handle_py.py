import requests
res = requests.get("http://api.open-notify.org/astros")
print(res.json())