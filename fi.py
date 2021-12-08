from PIL import Image, ImageTk, ImageFilter, ImageDraw
import tkinter as tk
from tkinter import filedialog as fd
import cv2

im = None
op_img = None


## 파일 열기

def func_open():
    global im, op_img
    fname = fd.askopenfilename()
    im = Image.open(fname)
    op_img = ImageTk.PhotoImage(im)
    canvas.create_image(250, 250, image=op_img)
    window.update()

#프로그램 종료
def func_quit():
    window.destroy()

#엣지 강조 필터

def edge_filter():
    global im, op_img
    out = im.filter(ImageFilter.EDGE_ENHANCE)
    op_img = ImageTk.PhotoImage(out)
    canvas.create_image(250, 250, image=op_img)
    window.update()

#gray-scale

def gray_scale():
    global im, op_img
    out = im.convert('L')
    op_img = ImageTk.PhotoImage(out)
    canvas.create_image(250, 250, image=op_img)
    window.update()

def blur_filter():
    global im, op_img
    out = im.filter(ImageFilter.BLUR)
    op_img = ImageTk.PhotoImage(out)
    canvas.create_image(250, 250, image=op_img)
    window.update()



# 좌우반전/상하반전

def left_right():
    global im, op_img
    out = im.transpose(Image.FLIP_LEFT_RIGHT)
    op_img = ImageTk.PhotoImage(out)
    canvas.create_image(250, 250, image=op_img)
    window.update()




def rotate180():
    global im, op_img
    out = im.transpose(Image.ROTATE_180)
    op_img = ImageTk.PhotoImage(out)
    canvas.create_image(250, 250, image=op_img)
    window.update()




window = tk.Tk()
window.title("SHIN JIMIN")
canvas = tk.Canvas(window, width=500, height=500)
canvas.pack()

menuBAR = tk.Menu(window)
filemenu = tk.Menu(window)
toolMenu = tk.Menu(window)
resmenu = tk.Menu(window)
cropmenu = tk.Menu(window)

menuBAR.add_cascade(label="파일", menu=filemenu)
filemenu.add_command(label="열기", command=func_open)
filemenu.add_command(label="닫기", command=func_quit)

menuBAR.add_cascade(label="효과", menu=toolMenu)
toolMenu.add_command(label="엣지필터 적용", command=edge_filter)
toolMenu.add_command(label="흑백필터 적용", command=gray_scale)
toolMenu.add_command(label="블러필터 적용", command=blur_filter)

menuBAR.add_cascade(label="편집", menu=cropmenu)
cropmenu.add_command(label="좌우반전", command=left_right)
cropmenu.add_command(label="상하반전", command=rotate180)


window.config(menu=menuBAR)
window.mainloop()