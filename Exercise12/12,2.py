import requests

def weather():
    city = input("Enter municipality name: ")

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=ec69699252fcc9d5d15a431305c7ec26"

    response = requests.get(url)

    data = response.json()

    description = data["weather"][0]["description"]

    k = data["main"]["temp"]

    c = k - 273.15

    print(f"Weather in {city}: {description}")
    print(f"Temperature: {c}°C")

weather()