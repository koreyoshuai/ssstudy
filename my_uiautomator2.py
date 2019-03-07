# coding: utf-8
import uiautomator2 as u2
from time import sleep

# 连接
u = u2.connect('192.168.3.153')
d = u.session("com.fcmcoin.fcm")  # restart app

sleep(2)
d(resourceId="com.fcmcoin.fcm:id/navigation_news_pager").click()
d.toast.show("hello world",1.0)