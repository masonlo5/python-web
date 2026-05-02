#######################匯入模組#######################
# 匯入 ttkbootstrap 模組，這個美化版 tkinter 元件在 adv-02/prj-04-ttk_GUI.py 已經介紹過
from ttkbootstrap import *

# 匯入 sys、os 模組，用來設定工作目錄
import sys
import os

#######################設定工作目錄########################
# 工作目錄的設定方式在 adv-01/prj-08-loadmage.py 已經介紹過
os.chdir(sys.path[0])


#######################定義函數########################
# 顯示計算結果的函式
def show_result():
    # Entry 是單行輸入框，get() 可以取出使用者輸入的文字
    entry_text = entry.get()
    try:
        # 這裡用 eval() 直接計算簡單的數學字串，例如 1+2*3
        result = eval(entry_text)
    except:
        # 若輸入不是合法算式，就顯示錯誤訊息
        result = "計算錯誤"
    label.config(text=result)


#######################建立視窗########################
window = Tk()  # 建立視窗
window.title("My GUI")  # 設定視窗標題

#######################設定字型########################
# option_add() 設定預設字型的概念在 adv-02/prj-04-ttk_GUI.py 已經介紹過
font_size = 20
window.option_add("*font", ("Helvetica", font_size))

#######################設定主題########################
# Style 與按鈕樣式的設定在 adv-02/prj-04-ttk_GUI.py 已經介紹過
style = Style(theme="minty")
style.configure("my.TButton", font=("Helvetica", font_size))

#######################建立標籤########################
# Label 搭配 grid 的寫法在 adv-02/prj-04-ttk_GUI.py 已經介紹過
label = Label(window, text="計算結果")
label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

#######################建立Entry物件########################
# 建立第一個 Entry 輸入框，讓使用者輸入算式
entry = Entry(window, width=30)
entry.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

#######################建立按鈕########################
# Button 搭配 style 與 grid 的寫法在 adv-02/prj-04-ttk_GUI.py 已經介紹過
button = Button(window, text="顯示計算結果", command=show_result, style="my.TButton")
button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

#######################運行應用程式########################
window.mainloop()
