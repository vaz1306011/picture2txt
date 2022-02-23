import os

import numpy


def picture2txt(paths: list, width: int) -> list:
    import numpy as np
    from PIL import Image
    if width <= 0:
        raise ValueError("寬度必須是正整數")
    if not paths:
        raise ValueError("路徑為空")
    file = []
    for im in paths:
        path = im
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
        name_end = path.rfind('.')
        name_front = path.rfind('/', 0, name_end-1)
        name = path[name_front+1:name_end]
        file.append([name, arr])

    return file


if __name__ == '__main__':
    try:
        width = int(input("輸入txt寬度:"))
        import tkinter as tk
        from tkinter import filedialog
        tk.Tk().withdraw()
        paths = filedialog.askopenfilenames(initialdir=".", title="選取圖片", filetypes=[
            ("圖片", "png jpeg jpg"), ("所有檔案", '*')])
        file = picture2txt(paths, width)

        for name, arr in file:
            if not os.path.isdir("./輸出"):
                os.mkdir("./輸出")
            with open(f'./輸出/{name}.txt', 'w') as fp:
                for line in arr.tolist():
                    fp.write(''.join(line))
                    fp.write('\n')
            print(f'{name}.txt 《輸出完成》')

    except ValueError as e:
        print(e)
    finally:
        os.system("pause")
