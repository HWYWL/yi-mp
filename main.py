import network,time

#初始化相关模块

#WIFI连接函数
def WIFI_Connect():
    wlan = network.WLAN(network.STA_IF) #STA模式
    wlan.active(True)                   #激活接口
    start_time=time.time()              #记录时间做超时判断

    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('JinKe_Test', 'jinke#2018pc')  # 输入WIFI账号密码

        while not wlan.isconnected():
            #超时判断,15秒没连接成功判定为超时
            if time.time()-start_time > 15 :
                print('WIFI Connected Timeout!')
                break

    if wlan.isconnected():

        #串口打印信息
        print('network information:', wlan.ifconfig())

        print('IP/Subnet/GW:',0,0)
        print(wlan.ifconfig()[0], 0, 20)
        print(wlan.ifconfig()[1],0,38)
        print(wlan.ifconfig()[2],0,56)

#执行WIFI连接函数
WIFI_Connect()
