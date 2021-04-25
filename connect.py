import requests
import socket
import pywifi
import time
from pywifi import const


def connect_wifi():
    wifi = pywifi.PyWiFi()  # 创建一个wifi对象
    ifaces = wifi.interfaces()[0]  # 取第一个无限网卡
    ifaces.disconnect()  # 断开网卡连接
    time.sleep(3)  # 缓冲3秒
    profile = pywifi.Profile()  # 配置文件
    profile.ssid = "NJUPT-CMCC"  # wifi名称
    ifaces.remove_all_network_profiles()  # 删除其他配置文件
    tmp_profile = ifaces.add_network_profile(profile)  # 加载配置文件

    ifaces.connect(tmp_profile)  # 连接
    return 1


connect_wifi()
time.sleep(3)  # 不加缓冲会无法post
ip = socket.gethostbyname(socket.gethostname())
url = 'http://p.njupt.edu.cn:801/eportal/?c=ACSetting&a=Login&protocol=http:&hostname=p.njupt.edu.cn&iTermType=1&wlanuserip=' + \
    ip+'&wlanacip=10.255.252.150&wlanacname=XL-BRAS-SR8806-X&mac=00-00-00-00-00-00&ip=' + \
    ip+'&enAdvert=0&queryACIP=0&loginMethod=1'
headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;'}
postdata = {
    'DDDDD': ',0,学号@cmcc',
    'upass': '密码',
}
requests.post(url, data=postdata)
