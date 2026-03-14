#######################匯入模組#######################
# import tkinter as tk
from tkinter import *


#######################定義函數########################
def say_fun():
    # 顯示訊息
    print("Hello, World!")
    display.config(text="Hello, World!", fg="blue", bg="yellow")


def clear_fun():
    display.config(text="", bg=window.cget("bg"))


#######################建立視窗########################
# 建立主視窗
window = Tk()
# 設定視窗標題
window.title("我的第一個GUI程式")


#######################建立按鈕########################
# 建立按鈕，並指定按下按鈕時要執行的函數
button = Button(window, text="Show screen", command=say_fun)
# 將按鈕放置在視窗中
button.pack()
button2 = Button(window, text="Clear screen", command=clear_fun)
button2.pack()

#########################建立標籤########################
# 創建一個標籤，顯示一些文字
# Label參數說明： (視窗名稱，顯示的文字，文字顏色，背景顏色)
display = Label(window, text="")
# 將標籤放置在視窗中
display.pack()

#######################運行應用程式########################
# 啟動事件循環
window.mainloop()
