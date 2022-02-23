# -*- coding: utf-8 -*-
# @Time     : 2021/5/13 12:06
# @Author   : Xia_fei
# @Name     : 圖片轉字元圖
# @Software : Visual Studio Code
# @Version  : 2.0

import numpy as np
from PIL import Image

width = int(input("輸入畫質:"))
while 1:
    try:
        name = input("輸入檔名:")
        im = Image.open(f"{name}")
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
        i = len(name)-1
        while name[i] != '.':
            i -= 1
        with open(f'{name[0:i]}.txt', 'w') as fp:
            for line in arr.tolist():
                fp.write(''.join(line))
                fp.write('\n')
        print("《輸出完成》")
    except:
        print("《輸入錯誤》")
        continue
