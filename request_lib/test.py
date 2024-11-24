import requests

city_name = "Kerman"

try:
    r = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=213f95374a9ee29ab7041cd44078c47e')

except Exception as e:
    print("Your city was wrong")

    print(e)


py_dict_weather = r.json()


print(f"{int(py_dict_weather['main']["temp"])-273} C")
