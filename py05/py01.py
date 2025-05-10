import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
# 设置窗口标题
root.title("Numb Tkinter")
# 设置窗口宽高,单位是像素pixel
w,h,x,y = 400, 300, 100, 100
# 获取屏幕宽度 : root.winfo_screenwidth()
#root.geometry("400x300+100+100")
root.geometry("%dx%d+%d+%d" % (w, h, x, y))
# 拖拽时可以设置的窗口最大宽高
root.maxsize(800, 600)
# 拖拽时可以设置的窗口最小宽高
root.minsize(100, 80)
# 设置窗口背景颜色
root.configure(bg="#D8E9DE")
# 更改默认窗口图标方式1
# root.iconbitmap("xx.ico")
# 更改默认窗口图标方式2
icon_image = Image.open("icon.png")
photo = ImageTk.PhotoImage(icon_image)
root.iconphoto(True, photo)
# Label( )方法可以用于在窗口内建立文字或图像标签
label = tk.Label(root, text="Tkinter is working!", fg="red", bg="white", height=2, width=20)
# 包装与定位组件
label.pack()
root.mainloop()
print("Hello World!")
