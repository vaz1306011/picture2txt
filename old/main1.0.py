# -*- coding: utf-8 -*-
# @Time     : 2021/5/13 12:08
# @Author   : Xia_fei
# @Name     : 圖片轉字元圖
# @Software : Visual Studio Code
# @Version  : 1.0

from PIL import Image
import numpy as np

name=input("輸入檔名:")
im = Image.open(f"{name}")
im = im.convert('L')
width = 720
height = int(width*im.size[1]/im.size[0]/2)
im=im.resize((width,height))
arr=np.array(im)
arr=255-arr

chs0=np.array([' ','.',',','-','^','~',':',';','!','+','=','*','#','$','&','@'])
arr=arr/16

chs1=np.array([' ','.',',',"'",'"','-','^','~',':',';','!','+','=','*','|','#','$','&','@']) #26▁▂▃▅▆▇█
#arr=arr/14

chs2=np.array(['　','．','，','－','︿','～','：','；','｜','！','＋','＝','＊','＃','＄','＆','＠','▆']) #26▁▂▃▅▆▇█
#arr=arr/15

chs3=np.array([' ','A','B',"C",'D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
#arr=arr/10

arr=arr.astype(np.uint8)
arr=chs0[arr]
with open(r'test.txt','w') as fp:
    for line in arr.tolist():
        fp.write(''.join(line))
        fp.write('\n')