import smtplib
from email.mime.text import MIMEText

class Send_Email:
    """
    send a Email
    """
    def __init__(self,SMTPSERVER,SENDER,RECIPENTS,PASSWD='123456',MESSAGE=None):
        self.smtpserver = SMTPSERVER
        self.sender = SENDER
        self.recipents = RECIPENTS
        self.passwd = PASSWD
        self.message = MESSAGE

    def send(self):
        #构建消息
        send_email = MIMEText(self.message)
        send_email["Subject"] = "Test Email"
        send_email["From"] = self.sender
        send_email["To"] = self.recipents
        #服务发送
        smtpserver = smtplib.SMTP(self.smtpserver,25)
        smtpserver.login(self.sender,self.passwd)
        smtpserver.sendmail(self.sender,self.recipents,send_email.as_string())
        smtpserver.quit()




SMTPServer = "smtp.163.com"
sender = "whxa@163.com"
passwd = "whr26"
message = "Hi this is a email for myself!"
recipients = "wanghon@wrdxa.com"

send_email = Send_Email(SMTPServer,sender,recipients,passwd,message)
send_email.send()

