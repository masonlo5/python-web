import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
from io import BytesIO

# =========================
# OpenWeather API Key
# =========================
API_KEY = "892da2f13edf3c7f382637760e72d224"  # API Key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"  # API URL
UNITS = "metric"  # 單位 (公制)
LANG = "zh_tw"  # 語言 (繁體中文)
ICON_BASE_URL = "http://openweathermap.org/img/wn/"  # 天氣圖示的基礎 URL

# =========================
# 取得天氣資訊
# =========================
def get_weather():
    city = city_entry.get()

    if not city:
        messagebox.showwarning("提醒", "請輸入城市名稱")
        return

    # 判斷溫度單位
    if unit_var.get():
        units = "metric"
        unit_symbol = "°C"
    else:
        units = "imperial"
        unit_symbol = "°F"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units={units}&lang=zh_tw"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            messagebox.showerror("錯誤", "找不到城市")
            return

        # 取得資料
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        icon_code = data["weather"][0]["icon"]

        # 更新文字
        temp_label.config(text=f"溫度: {temp}{unit_symbol}")
        desc_label.config(text=f"描述: {description}")

        # 下載天氣圖示
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
        icon_response = requests.get(icon_url)

        image_data = icon_response.content
        image = Image.open(BytesIO(image_data))
        photo = ImageTk.PhotoImage(image)

        icon_label.config(image=photo)
        icon_label.image = photo

    except Exception as e:
        messagebox.showerror("錯誤", str(e))

# =========================
# GUI 視窗
# =========================
root = tk.Tk()
root.title("天氣查詢系統")
root.geometry("650x300")
root.configure(bg="white")

# =========================
# 城市輸入
# =========================
city_text = tk.Label(root, text="請輸入想搜尋的城市:", font=("微軟正黑體", 14), bg="white")
city_text.pack(pady=10)

city_entry = tk.Entry(root, width=30, font=("Arial", 14))
city_entry.pack()

# =========================
# 查詢按鈕
# =========================
search_btn = tk.Button(
    root,
    text="獲得天氣資訊",
    font=("微軟正黑體", 12),
    bg="#8FD3C1",
    fg="white",
    command=get_weather
)
search_btn.pack(pady=10)

# =========================
# 天氣圖示
# =========================
icon_title = tk.Label(root, text="天氣圖標", font=("微軟正黑體", 14), bg="white")
icon_title.pack()

icon_label = tk.Label(root, bg="white")
icon_label.pack()

# =========================
# 溫度與描述
# =========================
temp_label = tk.Label(root, text="溫度: ?°C", font=("微軟正黑體", 16), bg="white")
temp_label.pack(pady=5)

desc_label = tk.Label(root, text="描述: ?", font=("微軟正黑體", 16), bg="white")
desc_label.pack(pady=5)

# =========================
# 單位切換
# =========================
unit_var = tk.BooleanVar()
unit_var.set(True)

unit_check = tk.Checkbutton(
    root,
    text="溫度單位(°C/°F)",
    variable=unit_var,
    font=("微軟正黑體", 12),
    bg="white"
)
unit_check.pack(pady=10)

# =========================
# 啟動
# =========================
root.mainloop()