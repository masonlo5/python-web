#######################匯入模組#######################
# requests 可以幫我們向網站或 API 發送請求
import requests

#######################定義常數########################
API_KEY = "892da2f13edf3c7f382637760e72d224"  # API Key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"  # API URL
UNITS = "metric"  # 單位 (公制)
LANG = "zh_tw"  # 語言 (繁體中文)

#######################主程式########################
city_name = "taipei"

# 把 API 網址、金鑰、城市、單位與語言組合成完整請求網址
send_url = f"{BASE_URL}appid={API_KEY}&q={city_name}&units={UNITS}&lang={LANG}"

print(f"發送的 URL：{send_url}")  # 印出發送的 URL

# requests.get(url) 會對這個網址發送 HTTP GET 請求，向伺服器拿資料
response = requests.get(send_url)

# response.json() 會把回傳的 JSON 資料轉成 Python 字典，之後就能用鍵值取資料
info = response.json()

# 處理和顯示天氣資訊
if "weather" in info and "main" in info:
    current_temperature = info["main"]["temp"]
    weather_description = info["weather"][0]["description"]

    print(f"城市：{city_name}")
    print(f"溫度：{current_temperature}°C")
    print(f"描述：{weather_description}")
else:
    print("找不到該城市或無法獲取天氣資訊")
