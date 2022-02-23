# -*- coding: utf-8 -*-
# @Time     : 2021/5/13 12:08
# @Author   : Xia_fei
# @Name     : 圖片轉字元圖
# @Software : Visual Studio Code
# @Version  : 3.0
import os
import tkinter as tk
from tkinter import filedialog

import numpy as np
from PIL import Image

root = tk.Tk()
root.withdraw()
while True:
    try:
        width = int(input("輸入畫質:"))
        if width <= 0:
            break
        address = filedialog.askopenfilenames(initialdir="./", title="選取圖片")
        for im in address:
            name = im
            im = Image.open(im)
            im = im.convert('L')
            height = int(width*im.size[1]/im.size[0]/2)
            im = im.resize((width, height))
            arr = np.array(im)
            arr = 255-arr
            chs0 = np.array([' ', '.', ',', '-', '^', '~', ':', ';',
                             '!', '+', '=', '*', '#', '$', '&', '@'])
            arr = arr/16
            arr = arr.astype(np.uint8)
            arr = chs0[arr]
            end = len(name)-1
            while name[end] != '.':
                end -= 1
            front = end-1
            while name[front] != '/':
                front -= 1
            if not os.path.isdir("./輸出"):
                os.mkdir("./輸出")
            with open(f'./輸出/{name[front+1:end]}.txt', 'w') as fp:
                for line in arr.tolist():
                    fp.write(''.join(line))
                    fp.write('\n')
            print(f'{name[front+1:end]}.txt 《輸出完成》')
        print()
    except:
        print("《輸入錯誤》")
        continue
