import smtplib
import email.mime.multipart
import email.mime.text

msg = email.mime.multipart.MIMEMultipart()
'''
最后终于还是找到解决办法了：邮件主题为‘test’的时候就会出现错误，换成其他词就好了。。我也不知道这是什么奇葩的原因
'''
msg['Subject'] = 'duanx'
msg['From'] = 'deonnejiang@163.com'
msg['To'] = 'danyang.rainbow@outlook.com'
content = '''''
    来个图片啥的吧，还可以画个图
    asdfsfsdf
    asdfsdfsdfsdf
    啊手动阀手动阀
'''
txt = email.mime.text.MIMEText(content)
msg.attach(txt)

# smtp = smtplib
smtp = smtplib.SMTP()
smtp.connect('smtp.163.com', '25')
smtp.login('deonnejiang@163.com', '970227jdY')
y = smtp.sendmail('deonnejiang@163.com', 'danyang.rainbow@outlook.com', msg.as_string())
smtp.quit()
print('邮件发送成功email has send out !')





