#######################匯入模組#######################
from tkinter import *
from PIL import Image, ImageTk

# pip install pillow
import sys
import os

#######################設定工作目錄#######################
# 取得目前檔案的絕對路徑
os.chdir(sys.path[0])

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
#######################運行應用程式########################
# 啟動事件循環
window.mainloop()
