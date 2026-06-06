import requests

API_KEY = "892da2f13edf3c7f382637760e72d224"
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast?"
UNITS = "metric"
LANG = "zh_tw"

city_name = "Taipei"
send_url = f"{BASE_URL}appid={API_KEY}&q={city_name}&units={UNITS}&lang={LANG}"
print(f"發送的 URL：{send_url}")
response = requests.get(send_url)
response.raise_for_status()
info = response.json()

if"city" in info:
    for forecast in info["list"]:
        dt_txt = forecast["dt_txt"]
        temp = forecast["main"]["temp"]
        weather_description = forecast["weather"][0]["description"]

        print(dt_txt, temp, weather_description)

else:
    print("無法找到該城市的天氣資訊。")