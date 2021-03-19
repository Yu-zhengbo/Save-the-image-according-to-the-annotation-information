import matplotlib.pyplot as plt

file_txt = r'C:\Users\ASUS\Desktop\pic_json\label.txt'

def read_txt(file):
    with open(file, encoding='utf-8') as f:
        s = f.read()
        s = s.split()
        # print(s)
        a = []
        for i in s:
            a.append(i.split('，'))
        for i in a:
            for j in range(len(i)):
                i[j] = int(i[j])
        return a
# print(read_txt(file_txt))


file = r'C:\Users\ASUS\Desktop\pic_json'
import os
import re
# print(os.listdir(file))
png = []
txt = []
for i in os.listdir(file):
    if re.search(r'\.png',i):
        png.append(i)
    else:
        txt.append(i)
# print(png,txt)

for i in png:
    pic_file = file+'\\'+i
    txt_file = file+'\\'+i[:-4]+'.txt'
    location = read_txt(txt_file)
    img = plt.imread(pic_file)
    q = 0
    for j in location:
        q += 1
        img1 = img[j[0]:j[2],j[1]:j[3],:]
        plt.imsave('{0}\\{1}{2}.png'.format(file,i,q),img1)

    print(location)