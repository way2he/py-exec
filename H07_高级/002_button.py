import tkinter as tk
from tkinter import messagebox

def create_button(parent, text, callback_data):
    # 闭包绑定回调数据
    def on_click():
        messagebox.showinfo("提示", f"点击了{text}，携带数据：{callback_data}")
    btn = tk.Button(parent, text=text, command=on_click)
    return btn

root = tk.Tk()
# 创建两个按钮，分别绑定不同数据
btn1 = create_button(root, "按钮A", "用户A")
btn2 = create_button(root, "按钮B", "用户B")
btn1.pack()
btn2.pack()
root.mainloop()