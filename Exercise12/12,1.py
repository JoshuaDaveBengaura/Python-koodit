import requests

def joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    data = response.json()
    return data["value"]

joke = joke()
print(joke)