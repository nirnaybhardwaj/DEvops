import requests

API_KEY = '3bf2e02225d18f7f41445e394e101ce2'
city_name = input("Enter the the city name: ")


url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'

# response = requests.get(url)
# print(response)

# if response.status_code == 200:
    # weather_data = response.json()
    # print(weather_data)



