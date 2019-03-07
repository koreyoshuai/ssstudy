import yagmail

# 连接邮箱服务器
yag = yagmail.SMTP(user="zhangmengshuai835@163.com",password="Zms63519115",host='smtp.163.com',port='25')

# 发送邮件
yag.send(to='408612073@qq.com',subject='test',contents='just test')