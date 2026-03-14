#######################匯入模組#######################
from tkinter import *
import random


#######################定義函數########################
def say_fun():
    fg_COLORS = "#" + "".join([random.choice("0123456789ABCDEF") for j in range(6)])
    """
    
    fg_COLORS = "#"
    for j in range(6):
        fg_COLORS += random.choice("0123456789ABCDEF")
    """

    bg_COLORS = "#" + "".join([random.choice("0123456789ABCDEF") for j in range(6)])
    display.config(text="Hello, World!", fg=fg_COLORS, bg=bg_COLORS)


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

#########################建立標籤########################
# 創建一個標籤，顯示一些文字
# Label參數說明： (視窗名稱，顯示的文字，文字顏色，背景顏色)
display = Label(window, text="")
# 將標籤放置在視窗中
display.pack()

#######################運行應用程式########################
# 啟動事件循環
window.mainloop()
