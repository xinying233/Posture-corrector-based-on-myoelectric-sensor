该设备利用Arduino作为数据采集端，接收外界的肌电模块收集的肩颈部位肌肉信号，并稍作处理后通过蓝牙模块传输到PC端。
PC端接收信号利用python进行数据处理，绘制出踩点下的肌电信号图像并加入弹窗提醒功能，从而实现驼背提醒功能。

PS：我们后期可能会使用树莓派作为数据采集端以收集更多数据并进行数据分析。

This deviece is a posture corrector based on myoelectric sensor. The data from the myoelectric sensor will be directly sent to Arduino, and the signal will be sent wirelessly by bluetooth. We use PC to collect the data and process it on python, which will draw the signal image and "pop up" the remind window. It can remind people who sit with an unhealthy posture in front of the computer for a long time.

Ps: We might use Raspberry pi to improve the device.
