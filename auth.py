# -*- coding:utf-8 -*-

import cv2
import numpy as np
import os

np.set_printoptions(threshold='nan', linewidth=10000)  # 全部输出, 每行最长10000个字符

def quzao(im_src):
    img = im_src
    list1 = []
    for i in xrange(img.shape[0]):
        for j in xrange(img.shape[1]):    # 去掉背景色（把三个通道值均在180以上的认为是背景）
            if img[i, j, 0] > 180 and img[i, j, 0] > 180 and img[i, j, 0] > 180:
                img[i, j, ] = 0
            else:
                list1.append(img[i, j, ])
    b_list = []
    g_list = []
    r_list = []
    for j in xrange(len(list1)):
        b_list.append(list1[j][0])
        g_list.append(list1[j][1])
        r_list.append(list1[j][2])
    b_mean = np.mean(b_list)        # 求RGB三通道下各个通道的颜色均值
    g_mean = np.mean(g_list)
    r_mean = np.mean(r_list)
    m = img.shape[0]
    n = img.shape[1]
    pic_array = np.zeros((m, n))   # 初始化二维映射矩阵，用0填充
    for ii in xrange(m):       # 三个通道颜色与各自均值的差的绝对值和大于120的认为是背景色或噪音色
        for jj in xrange(n):
            if sum([abs(img[ii, jj, 0] - b_mean), abs(img[ii, jj, 1] - g_mean),abs(img[ii, jj, 2] - r_mean)]) > 120:
                img[ii, jj, ] = 0
            else:
                pic_array[ii, jj] = 1    # 非背景色与噪音色的地方，二维矩阵用1填充
    return pic_array.reshape(1, -1)[0]   # 将单个图片的二维矩阵拉伸为一维矩阵

def savedata(data, label):
    if label == '+':
        label = -1.0
    elif label == '*':
        label = -2.0
    else:
        label = float(label)
    with open('data.csv', 'a') as f:
        f.write(str(label) + ' ' + str(data).replace('[', '').replace(']', '') + '\n')

root = './pic/'
for picname in os.listdir(root):
    print picname
    if picname.endswith('.jpg'):
        im = cv2.imread(root + picname)
        im1 = quzao(im[8:25, 9:21, ])
        im2 = quzao(im[8:25, 23:35, ])
        im3 = quzao(im[8:25, 36:48, ])
        savedata(im1, picname[0])
        savedata(im2, picname[1])
        savedata(im3, picname[2])

# npdata = np.loadtxt('data.csv', dtype=float, comments=',')
# print npdata
