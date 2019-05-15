
# -*- coding: utf-8 -*-
import easygui as g
import serial
import matplotlib.pyplot as plt
import numpy as np
import time
import re
from scipy import signal
import seaborn
import struct
import sys

serialport = serial.Serial('COM9', 9600) # 串口配对（蓝牙数据为COM9输出）
if serialport.isOpen():
    print("open success") # 串口打开成功
else:
    print("open failed") # 串口打开失败

plt.grid(True)  # 添加网格
plt.ion()
plt.figure(1)
plt.xlabel('times') # 横轴Label
plt.ylabel('data') # 纵轴Label
plt.title('Diagram of The signal from SEMG') # 图像标题
t = [0] # 数据初始化
m = [0]
i = 0
intdata = 0
data = ''
count = 0
n = 0

while True:
    if i > 1000:# 1000次后清零
        plt.close('all')
        del t [:]
        del m [:] # 数据清空
        i = 0
        plt.cla()
        plt.grid(True)
    count = serialport.inWaiting()
    if n >= 80          :
       if n == 80: # 取第80个点为reference
          ref = pdata
       if abs(ref-pdata) >= 0.1 and  n % 40 == 0:# 每在40倍数时开始验证是否需要弹窗提醒
          mes = g.msgbox(msg='你驼背了!', title='SEMG muscle', ok_button='I know, 我已坐好')
          plt.close('all')
          del t[:] # 弹窗后清空图像和数据
          del m[:]
          i = 0
          n = 0
          plt.cla()
          plt.pause(3)
          plt.grid(True)
    if count > 0:
        data = serialport.readline(2) # 读取头两个数据检测是否为验证数据
        while data == b'AA':
          data=serialport.readline(3) # 数据验证成功，读取电压数据
          if data != '': # 如果数据不为空，则进行绘图
            print('%s' % (data))

            i = i + 1
            n = n + 1
            t.append(i)
            intdata=int(data)
            pdata=float((intdata-100)/100) # 对原数据进行还原
            round(pdata,2)
            m.append(pdata)
            plt.ylim((0,2.2)) # 固定y轴
            plt.plot(t, m, '-r') # 绘制图像
            plt.draw()

          plt.pause(0.05)  # 绘图频率


