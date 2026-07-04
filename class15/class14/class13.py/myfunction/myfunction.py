###############################匯入模組###############################
import requests
import openai


###############################定義類別###############################
# 定義一個類別，名稱為 MyFunction
# 這個類別將包含一些方法，用於執行特定的功能
# 目前這個類別沒有任何屬性或方法，但你可以根據需要添加它們
class WeatherAPI:
    """把 OpenWeather 的查詢流程包裝成一個類別，讓使用者可以更方便地使用"""

    def __init__(self, api_key, lang="zh_tw"):
        self.api_key = api_key
        self.units = "metric"
        self.lang = lang
        self.base_url = "https://api.openweathermap.org/data/2.5/weather?"
        self.forcecast_url = "https://api.openweathermap.org/data/2.5/forecast?"
        self.icon_url = "https://openweathermap.org/img/wn/"

    def get_current_weather(self, city_name):

        send_url = f"{self.base_url}appid={self.api_key}&q={city_name}&units={self.units}&lang={self.lang}"

        response = requests.get(send_url)
        return response.json()

    def get_weather_summary(self, city_name):
        info = self.get_current_weather(city_name)

        if "weather" in info and "main" in info:
            return {
                "city_name": info.get("name", city_name),
                "temperature_celslus": round(info["main"]["temp"], 2),
                "description": info["weather"][0]["description"],
                "icon_code": info["weather"][0]["icon"],
            }

        return None

    def get_icon_url(self, icon_code):

        return f"{self.icon_url}{icon_code}@2x.png"

    def get_icon(self, icon_code):
        url = self.get_icon_url(icon_code)
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        return None

    def get_forecast(self, city_name):

        send_url = (
            f"{self.forcecast_url}q={city_name}&appid={self.api_key}"
            f"&units={self.units}&lang={self.lang}"
        )

        response = requests.get(send_url)
        response.raise_for_status()
        return response.json()

    def get_forecast_summary(self, city_name, count=10):
        forecast_count = max(0, count)
        try:
            info = self.get_forecast(city_name)
        except requests.HTTPError as error:
            response = error.response
            if response is not None and response.status_code == 404:
                return None
            raise
        if "city" not in info or "list" not in info:
            return None
        city_label = info["city"].get("name", city_name)
        forecast_summary = []

        for forecast in info["list"][:forecast_count]:
            forecast_summary.append(
                {
                    "city_name": city_label,
                    "datetime": forecast["dt_txt"],
                    "temperature_celslus": round(forecast["main"]["temp"], 2),
                    "description": forecast["weather"][0]["description"],
                    "icon_code": forecast["weather"][0]["icon"],
                }
            )

        return forecast_summary


class AIAssistant:
    """一個簡單的 AI 助手類別，提供基本的對話功能"""

    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = api_key

    def ask(
        self,
        system_prompt,
        user_message,
        history_messages=None,
        temperature=0.2,
        model="gpt-4o",
    ):

        if not self.api_key:
            return None, "API 金鑰未設定，請聯繫管理員。"

        if history_messages is None:
            history_messages = []

        messages = (
            [{"role": "system", "content": system_prompt}]
            + history_messages
            + [{"role": "user", "content": user_message}]
        )

        try:
            response = openai.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature,
            )

            assistant_message = response.choices[0].message.content
            return assistant_message, None

        except Exception as e:
            return None, f"無法取得回應，請稍後再試。錯誤訊息: {e}"
