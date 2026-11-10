import requests

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url)

user1 = response.json()

print(user1["name"])
print(user1["email"])
print(user1["address"]["city"])