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


# 自動動畫變數
circle_dx = 5
circle_dy = 3
rect_dx = 4
rect_dy = 2


def animate_circle():
    global circle_dx, circle_dy
    canvas.move(circle, circle_dx, circle_dy)

    # 獲得圓形座標
    coords = canvas.coords(circle)

    # 檢查邊界並反彈
    if coords[0] <= 0 or coords[2] >= 600:
        circle_dx = -circle_dx
    if coords[1] <= 0 or coords[3] >= 600:
        circle_dy = -circle_dy

    window.after(50, animate_circle)


def animate_rect():
    global rect_dx, rect_dy
    canvas.move(rect, rect_dx, rect_dy)

    # 獲得矩形座標
    coords = canvas.coords(rect)

    # 檢查邊界並反彈
    if coords[0] <= 0 or coords[2] >= 600:
        rect_dx = -rect_dx
    if coords[1] <= 0 or coords[3] >= 600:
        rect_dy = -rect_dy

    window.after(50, animate_rect)


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

# 啟動動畫
animate_circle()
animate_rect()
#######################運行應用程式########################
# 啟動事件循環
window.mainloop()
