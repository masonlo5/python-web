#######################匯入模組#######################
from tkinter import *
from PIL import Image, ImageTk

# pip install pillow
import sys
import os

#######################設定工作目錄#######################
# 取得目前檔案的絕對路徑
os.chdir(sys.path[0])


def move_circle(event):
    key = event.keysym
    print(key)
    if key == "Right":
        canvas.move(circle, 10, 0)
    elif key == "Left":
        canvas.move(circle, -10, 0)
    elif key == "Up":
        canvas.move(circle, 0, -10)
    elif key == "Down":
        canvas.move(circle, 0, 10)


def move_rect(event):
    key = event.keysym
    print(key)
    if key == "d" or key == "D":
        canvas.move(rect, 10, 0)
    elif key == "a" or key == "A":
        canvas.move(rect, -10, 0)
    elif key == "w" or key == "W":
        canvas.move(rect, 0, -10)
    elif key == "s" or key == "S":
        canvas.move(rect, 0, 10)


def handle_keys(event):
    move_circle(event)
    move_rect(event)


#######################建立視窗########################
# 建立主視窗
window = Tk()
# 設定視窗標題
window.title("我的第一個GUI程式")

canvas = Canvas(window, width=600, height=600, bg="white")

canvas.pack()
#######################設定視窗圖片#######################
# 設定視窗圖示
window.iconbitmap("brawlstar.jpg")

#######################載入圖片#######################
# img = PhotoImage(file="brawlstar.jpg")
image = Image.open("brawlstar.jpg")
# Pil Image 轉換成 Tkinter 可用的圖片格式
img = ImageTk.PhotoImage(image)

#######################顯示圖片#######################
my_img = canvas.create_image(300, 300, image=img)

#######################畫圖形#######################
circle = canvas.create_oval(250, 150, 300, 200, fill="red")

rect = canvas.create_rectangle(220, 400, 340, 430, fill="blue")
msg = canvas.create_text(300, 100, text="brawlstar", fill="black", font=("Arial", 30))

#######################運行應用程式########################
# 啟動事件循環
window.mainloop()
