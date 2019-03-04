# 20、使用python给自己qq邮箱发送一份邮件
# '''参考源码及<<python参考手册>>'''
import smtplib
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

FORMAT = '%(asctime)s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)


class qEmail:
    _SERVER = smtplib.SMTP_SSL('smtp.qq.com', 465)

    def __init__(self):
        self.msg = MIMEMultipart()
        self.writing()
        # self.msg = MIMEText(self.text)

    def writing(self):
        self.frm = "1039427541@qq.com"  # input('From>>>')
        self.to = "hoyunk@foxmail.com"  # input('To>>>')
        self.subject = "test it"  # input('主题>>>')
        self.text = "hello"  # input('正文>>>')
        self.msg['from'] = self.frm
        self.msg['to'] = self.to
        self.msg['subject'] = self.subject
        self.msg.attach(MIMEText(self.text))
        return self

    def send_mail(self, password='qqcuiafvmcgmbeac'):
        try:
            self._SERVER.login(self.frm, password)
            self._SERVER.sendmail(self.frm, self.to, self.msg.as_string())
            logging.info('The Email send successfully')
        except:
            logging.warning('Failed to send.please check your FromAddress,ToAddress,Password')
        finally:
            self._SERVER.quit()


mail = qEmail()
mail.send_mail()