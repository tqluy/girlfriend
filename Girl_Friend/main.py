import time
import cv2
import numpy as np

i=1
while i!="01/08/2000":
    print("Nhập Ngày Sinh Người Yêu Bạn Đi:")
    i = input()
    while i != "01/08/2000":
        print("Nhập Sai Sinh Nhật Người Yêu Rồi! Nhập Lại <3")
        i = input()        
    else:
        print("Loading 10% ...")
        time.sleep(2)
        print("Loading 20% ...")
        time.sleep(0.7)
        print("Loading 40% ...")
        time.sleep(1.4)
        print("Loading 50% ...")
        time.sleep(0.6)
        print("Loading 60% ...")
        time.sleep(0.8)
        print("Loading 80% ...")
        time.sleep(1.5)
        print("Loading 100% ...")        
        time.sleep(0.2)


        image = cv2.imread('girlfriend.jpg', 0)
        new_width = int(image.shape[1]/10)
        new_height = int(image.shape[1]/10)
        image=cv2.resize(image,(new_width,new_height))
        charmap = "DZP:.57EMXQ"
        with open("girl.txt", 'w', encoding='utf-8') as f:
            for i, row in enumerate(image):
                for j, col in enumerate(row):
                    c = int((255 - col)*11 / 256)
                    f.write(charmap[c])
                    print(charmap[c], end='')
                print(charmap[c], end='')
                print('\n', end='')
                f.write('\n')
                time.sleep(0.05)
            f.close()
        break    


