import tkinter as tk
import tkinter.messagebox as mb

root = tk.Tk()
root.withdraw()

mb.showinfo('表白', '我喜欢你')
mb.showinfo('表白', '我喜欢你很久了')

while True:
    a = mb.askyesnocancel('表白', '做我女朋友好吗？', icon='question')
    if not a:
        mb.showerror('表白', '再想想好吗？')
    else:
        break

while True:
    b = mb.askokcancel('表白', '今年七夕一起过，好吗？', icon='question')
    if not b:
        mb.showerror('表白', '再想想吧')
    else:
        break

mb.showinfo('表白', '太好了\n现在你是我女朋友了')
mb.showinfo('表白', '不许告诉别人哦')
""""
版权声明：本文为CSDN博主「H_612」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_52132159/article/details/119545668"""
