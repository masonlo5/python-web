#######################匯入模組#######################
from tkinter import *


#######################建立視窗########################
# 建立主視窗
window = Tk()
# 設定視窗標題
window.title("我的第一個GUI程式")

canvas = Canvas(window, width=600, height=600, bg="white")

canvas.pack()

#######################運行應用程式########################
# 啟動事件循環
window.mainloop()
