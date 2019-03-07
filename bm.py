# coding: utf-8
import uiautomator2 as u2
from time import sleep

# 连接
u = u2.connect('192.168.3.153')
d = u.session("com.fcmcoin.fcm")  # restart app


sleep(2)
# 测试资讯模块
d(resourceId="com.fcmcoin.fcm:id/navigation_news_pager").click()
print("---进入资讯页面---")
sleep(3)
print("---测试轮播图---")
d(resourceId="com.fcmcoin.fcm:id/bannerTitle").click()
sleep(3)
d.swipe(0.4, 0.8,0.4, 0.1)
sleep(3)
d.swipe(0.4, 0.8,0.4, 0.1)
sleep(3)
d(resourceId="com.fcmcoin.fcm:id/iv_finish").click()
print("---轮播图测试通过---")
sleep(3)
d(text='快讯').click()
print("---进入快讯页面---")
sleep(3)
print("---展开第一条快讯---")
d(resourceId="com.fcmcoin.fcm:id/expandable_text").click()
sleep(3)
d.swipe(0.4, 0.8,0.4, 0.1)
print("---展开第二条快讯---")
d(resourceId="com.fcmcoin.fcm:id/expandable_text").click()
sleep(3)
print("---收缩第二条快讯---")
d(resourceId="com.fcmcoin.fcm:id/expandable_text").click()
sleep(3)
print("---拖动导航栏---")
d.swipe(0.9, 0.14,0.1, 0.14,0.5)
sleep(3)
d(text='矿圈').click()
print("---拖动导航栏成功---")
sleep(3)
d(resourceId="com.fcmcoin.fcm:id/textView").click()
print("---进入矿圈详情页面---")
sleep(3)
d.swipe(0.4, 0.8,0.4, 0.1)
sleep(3)
d.swipe(0.4, 0.8,0.4, 0.1)
sleep(3)
d(resourceId="com.fcmcoin.fcm:id/iv_finish").click()
print("---资讯测试结束---")

# 测试论坛模块
sleep(3)
d(resourceId='com.fcmcoin.fcm:id/navigation_forum').click()
sleep(2)
d(resourceId="com.fcmcoin.fcm:id/write_post").click()
sleep(2)
# 判断是否登录账号
try:
    d(text="请输入手机号").set_text("15558207835")
except BaseException as e:
    print("已登录账号")
    d.press("back")
else:
    d(text="请输入登录密码").set_text("123456a")
    sleep(2)
    d(text="登录").click()

# 浏览页面
d(resourceId="com.fcmcoin.fcm:id/textView4").click()
print("---进入论坛详情---")
sleep(3)
d.swipe(0.4, 0.8,0.4, 0.1)
sleep(2)
d.swipe(0.4, 0.8,0.4, 0.1)
d(resourceId="com.fcmcoin.fcm:id/editText").set_text("1")
sleep(2)
# 评论
d(resourceId="com.fcmcoin.fcm:id/textView6").click()
sleep(2)
# 帖子点赞
d(resourceId="com.fcmcoin.fcm:id/imageView3").click()
d.press("back")
print("---返回到推荐页面--")
# 推荐页面评论
d(resourceId="com.fcmcoin.fcm:id/imageView3").click()
sleep(2)
d(text="请发表你的观点").set_text("1")
d(resourceId="com.fcmcoin.fcm:id/button").click()
# 推荐页面点赞
sleep(2)
d(resourceId="com.fcmcoin.fcm:id/imageView2").click()

# 点击发帖按钮
d(resourceId="com.fcmcoin.fcm:id/write_post").click()
sleep(2)
try:
    d(text=u"已加入", className="android.widget.Button").click()
except BaseException as e:
    print("未加入社群")
else:
    d(resourceId="android:id/button1").click()
sleep(2)
d(text="其他").click()
d(text="加入").click()
sleep(2)
d(text="加入").click()
sleep(2)
d(text="已加入").click()
# 发帖
print("---发布帖子---")
d.click(0.162, 0.317)
sleep(2)
d(resourceId="com.fcmcoin.fcm:id/editText").set_text("text")
d(text="发布").click()
sleep(2)
time=d(resourceId="com.fcmcoin.fcm:id/textView2").get_text()
try:
    assert (time=="刚刚")
except AssertionError as msg:
    print("帖子发布失败")
else:
    print("帖子发布成功")
sleep(2)

d(text="关注").click()
d.click(0.243, 0.288)
print("---进入社区主页---")
name=d(resourceId="com.fcmcoin.fcm:id/textView").get_text()
news=d(resourceId="com.fcmcoin.fcm:id/textView2").get_text()
fans=d(resourceId="com.fcmcoin.fcm:id/textView4").get_text()
print(name+" 帖子数:"+news+" 粉丝数:"+fans)
d.swipe(0.4, 0.8,0.4, 0.1)
d(description=u"转到上一层级").click()
print("---社区测试结束---")

# 测试行情模块
# 切换到综合列表页面
sleep(2)
print("---测试行情页面---")
d(resourceId="com.fcmcoin.fcm:id/navigation_quote").click()
print("---测试市值/涨幅--")
d(text='市值/涨幅').click()
sleep(2)
d(resourceId="com.fcmcoin.fcm:id/name").click()
d.swipe(0.431, 0.947,0.431,0.447)
sleep(2)
d(text='简况').click()
sleep(2)
d(text='市场').click()
sleep(2)
d(resourceId="com.fcmcoin.fcm:id/name").click()
sleep(2)
exchange=d(resourceId="com.fcmcoin.fcm:id/exchange").get_text()
trade_pair_name=d(resourceId="com.fcmcoin.fcm:id/trade_pair_name").get_text()
print("---进入"+exchange+"交易所"+trade_pair_name+"交易对的行情详情页面---")
d(text='分时').click()
sleep(3)
d.swipe(0.696, 0.504,0.3,0.504)
quote_time=d(resourceId="com.fcmcoin.fcm:id/time").get_text()
quote_price=d(resourceId="com.fcmcoin.fcm:id/price").get_text()
quote_amount=d(resourceId="com.fcmcoin.fcm:id/amount").get_text()
print(quote_time+" 价格 "+quote_price+" 成交量 "+quote_amount)
sleep(2)
d(text='1天').click()
d.swipe(0.154, 0.529, 0.808, 0.566)
d.swipe(0.154, 0.529, 0.808, 0.566)
onedaytime=d(resourceId="com.fcmcoin.fcm:id/time").get_text()
onedayopen=d(resourceId="com.fcmcoin.fcm:id/open").get_text()
onedayclose=d(resourceId="com.fcmcoin.fcm:id/close").get_text()
onedayhigh=d(resourceId="com.fcmcoin.fcm:id/high").get_text()
onddaylow=d(resourceId="com.fcmcoin.fcm:id/low").get_text()
print(onedaytime+"开盘价:"+onedayopen+"收盘价:"+onedayclose+"最高价:"+onedayhigh+"最低价:"+onddaylow)
sleep(2)
try:
    d(text='更多').click()
except BaseException as e:
    d(text='30分').click()
else:
    pass
d(text='30分').click()

# 切换指标
d(text='指标').click()
sleep(2)
d(text='BOLL').click()
d(text='指标').click()
sleep(2)
d(text='KDJ').click()
d(text='指标').click()
sleep(2)
d(text='VOL').click()
d.press("back")
sleep(2)
print("---"+exchange+"交易所"+trade_pair_name+"交易对的行情测试结束---")
d.press("back")
sleep(2)


# 切换到币种列表页面
print("---切换到币种页面---")
d.click(0.507, 0.067)
d(text="BTC").click()
sleep(2)
d(text="币安").click()
sleep(2)
d.press("back")
d(text="ETH").click()
sleep(2)


# 切换到平台列表页面
print("---切换到平台页面---")
d.click(0.664, 0.07)
d(text="火币PRO").click()
sleep(2)
d(resourceId="com.fcmcoin.fcm:id/name").click()
yz=d(resourceId="com.fcmcoin.fcm:id/exchange").get_text()
try:
    assert (yz=='火币Pro')
except AssertionError as msg:
    print("进入火币Pro列表失败")
else:
    print("成功进入火币Pro列表")
d.press("back")
sleep(2)

# 测试自选模块
print("---进入自选页面---")
sleep(2)
d.click(0.327, 0.066)
sleep(1)
d(text="自选").click()
sleep(2)
try:
    d(text="请先登录").click()
except BaseException as e:
    print("已登录账号")
else:
    sleep(2)
    d(text="请输入手机号").set_text("15558207835")
    d(text="请输入登录密码").set_text("123456a")
    sleep(1)
    d(text="登录").click()

m=30
# 点击添加自选
while m>0:
    try:
        d(text="添加自选").click()
    except BaseException as e:
        d.swipe(0.481, 0.795,0.481,0.295)
        m=m-1
    else:
        break



# 添加交易所品种
# 滑动自选导航栏
sleep(2)
d.swipe(0.795, 0.129,0.195, 0.129)
d(text="UPBIT").click()
zxname=d(resourceId="com.fcmcoin.fcm:id/name").get_text()
d(resourceId="com.fcmcoin.fcm:id/name").click()
sleep(2)
d(resourceId="com.fcmcoin.fcm:id/complete").click()
try:
    d(text=zxname).click()
except BaseException as e:
    print("删除" + zxname + "成功")
else:
    print("添加" + zxname + "成功")
    d.press("back")
print("---行情测试结束---")
sleep(2)


# 我的模块
print("---进入我的模块测试页面---")
d(resourceId="com.fcmcoin.fcm:id/navigation_my_center").click()
sleep(2)
d(text="在线客服").click()
sleep(1)
d(resourceId="message").set_text("1")
sleep(1)
d(resourceId="sendBtn").click()
sleep(2)
d(resourceId="com.fcmcoin.fcm:id/iv_finish").click()
sleep(2)
d(text="每日任务").click()
sleep(2)
d.click(0.494, 0.745)
sleep(2)
d.press("back")
d(text="消息中心").click()
sleep(2)
d.press("back")
d(text="联系我们").click()
sleep(1)
d.press("back")
d(text="退出登录").click()
try:
    d(text="点击登录").click()
except BaseException as e:
    print("账号退出失败")
else:
    print("账号退出成功")
print("---我的模块页面测试结束---")
sleep(2)
print("---币摩测试结束---")