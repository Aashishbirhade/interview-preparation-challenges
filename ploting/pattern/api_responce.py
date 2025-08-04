
import requests
a = requests.get("https://jsonplaceholder.typicode.com/posts/")
print(a.json())