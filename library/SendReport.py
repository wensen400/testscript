#!/usr/bin/python
# -*- coding: utf8 -*-
import smtplib
from email.mime.text import MIMEText

mailto_list = ["zhangjian@sogou-inc.com"]
mail_host = "smtp.163.com"  # 设置服务器
mail_user = "xxxx@163.com"  # 用户名
mail_pass = "xxxx"  # 口令
mail_postfix = "163.com"  # 发件箱的后缀


def send_mail(to_list, sub, reportpath):  # to_list：收件人；sub：主题；content：邮件内容
    file = open(reportpath, "rb")
    content = ""
    for line in file.readlines():
        content = content + line.replace("class='hiddenRow'", "")

    me = "TestCenter" + "<" + mail_user + ">"  # 这里的hello可以任意设置，收到信后，将按照设置显示
    msg = MIMEText(content, _subtype='html', _charset='gb2312')  # 创建一个实例，这里设置为html格式邮件
    msg['Subject'] = sub  # 设置主题
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)  # 连接smtp服务器
        s.set_debuglevel(1)
        s.login(mail_user, mail_pass)  # 登陆服务器
        s.sendmail(me, to_list, msg.as_string())  # 发送邮件
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False
		
if __name__ == '__main__':
    if send_mail(mailto_list, "TestResult", '../2016-07-07-13_29_15HTMLtemplate.html'):
        print u"发送成功"
    else:
        print u"发送失败"