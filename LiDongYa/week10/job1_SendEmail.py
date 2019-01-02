from email.mime.text import MIMEText
from email.header import Header
import smtplib


def send_email(from_addr:str, from_addr_psd:str, to_addr:str, smtp_host:str, smtp_post:int, subject:str, content:str):
    """
    :param from_addr:       发送者邮箱地址(用户登入)
    :param from_addr_psd:   SMTP登入密码，需进入邮箱设置
    :param to_addr:         接收者邮箱地址
    :param smtp_host:       主机地址
    :param smtp_post:       主机端口
    :param subject:         邮件主题
    :param content:         邮件内容
    :return:
    """

    # 构建邮件
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = from_addr
    msg['To'] = to_addr

    # 发送邮件
    smtp_client = smtplib.SMTP_SSL(smtp_host, smtp_post)
    smtp_client.set_debuglevel(1)
    smtp_client.login(from_addr, from_addr_psd)
    smtp_client.sendmail(from_addr, [to_addr], msg.as_string())
    smtp_client.quit()
    print('OK')


if __name__ == '__main__':
    smtp_host = 'smtp.126.com'
    from_addr = 'XXXXXX@126.com'
    from_addr_psd = 'XXXXXX'
    to_addr = 'XXXXX@qq.com'
    subject = 'Hello, Python'
    content = 'How are you?'
    send_email(from_addr, from_addr_psd, to_addr, smtp_host, 465, subject, content)

