import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
from io import BytesIO

# =========================
# OpenWeather API
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

    city = city_entry.get().strip()

    if city == "":
        messagebox.showwarning("提醒", "請輸入城市名稱")
        return

    # 溫度單位
    if unit_var.get():
        units = "metric"
        unit_symbol = "°C"
    else:
        units = "imperial"
        unit_symbol = "°F"

    # API URL
    url = (
        f"https://api.openweathermap.org/data/2.5/weather?"
        f"q={city}&appid={API_KEY}&units={units}&lang=zh_tw"
    )

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        # 城市不存在
        if str(data["cod"]) != "200":
            messagebox.showerror("錯誤", "找不到該城市")
            return

        # =========================
        # 取得資料
        # =========================
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        icon_code = data["weather"][0]["icon"]

        # 更新畫面
        temp_label.config(
            text=f"溫度: {round(temp, 1)}{unit_symbol}"
        )

        desc_label.config(
            text=f"描述: {description}"
        )

        # =========================
        # 顯示天氣圖示
        # =========================
        icon_url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"

        icon_response = requests.get(icon_url)

        image = Image.open(BytesIO(icon_response.content))

        # 調整圖片大小
        image = image.resize((100, 100))

        photo = ImageTk.PhotoImage(image)

        icon_label.config(image=photo)
        icon_label.image = photo

    except requests.exceptions.Timeout:
        messagebox.showerror("錯誤", "連線逾時")

    except requests.exceptions.ConnectionError:
        messagebox.showerror("錯誤", "無法連線到網路")

    except Exception as e:
        messagebox.showerror("錯誤", str(e))


# =========================
# GUI 視窗
# =========================
root = tk.Tk()

root.title("天氣查詢系統")
root.geometry("700x400")
root.configure(bg="white")

# =========================
# 標題
# =========================
title_label = tk.Label(
    root,
    text="天氣查詢系統",
    font=("微軟正黑體", 24, "bold"),
    bg="white",
    fg="#444"
)

title_label.pack(pady=15)

# =========================
# 搜尋區
# =========================
search_frame = tk.Frame(root, bg="white")
search_frame.pack(pady=10)

city_text = tk.Label(
    search_frame,
    text="請輸入想搜尋的城市:",
    font=("微軟正黑體", 14),
    bg="white"
)

city_text.grid(row=0, column=0, padx=5)

city_entry = tk.Entry(
    search_frame,
    width=25,
    font=("Arial", 14)
)

city_entry.grid(row=0, column=1, padx=5)

search_btn = tk.Button(
    search_frame,
    text="獲得天氣資訊",
    font=("微軟正黑體", 12),
    bg="#8FD3C1",
    fg="white",
    activebackground="#73c6b6",
    padx=10,
    command=get_weather
)

search_btn.grid(row=0, column=2, padx=10)

# =========================
# 結果區
# =========================
result_frame = tk.Frame(root, bg="white")
result_frame.pack(pady=20)

# 天氣圖示
icon_title = tk.Label(
    result_frame,
    text="天氣圖標",
    font=("微軟正黑體", 14),
    bg="white"
)

icon_title.grid(row=0, column=0, padx=40)

temp_title = tk.Label(
    result_frame,
    text="溫度",
    font=("微軟正黑體", 14),
    bg="white"
)

temp_title.grid(row=0, column=1, padx=40)

desc_title = tk.Label(
    result_frame,
    text="描述",
    font=("微軟正黑體", 14),
    bg="white"
)

desc_title.grid(row=0, column=2, padx=40)

# 圖示
icon_label = tk.Label(result_frame, bg="white")
icon_label.grid(row=1, column=0)

# 溫度
temp_label = tk.Label(
    result_frame,
    text="?",
    font=("Arial", 18),
    bg="white"
)

temp_label.grid(row=1, column=1)

# 描述
desc_label = tk.Label(
    result_frame,
    text="?",
    font=("微軟正黑體", 16),
    bg="white"
)

desc_label.grid(row=1, column=2)

# =========================
# 溫度單位
# =========================
unit_var = tk.BooleanVar()
unit_var.set(True)

unit_check = tk.Checkbutton(
    root,
    text="溫度單位 (°C / °F)",
    variable=unit_var,
    font=("微軟正黑體", 12),
    bg="white",
    command=get_weather
)

unit_check.pack(pady=15)

# =========================
# Enter 鍵搜尋
# =========================
root.bind("<Return>", lambda event: get_weather())

# =========================
# 啟動
# =========================
root.mainloop()