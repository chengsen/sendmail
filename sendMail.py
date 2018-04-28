from email.header import Header
from email.mime.text import MIMEText
from smtplib import SMTP_SSL


class Mail():
    def __init__(self, receivers, mail_host, mail_user, mail_pass, mail_name=None):
        """
        :param receivers:
        :param mail_host: the server url of your mail
        :param mail_user: your mail for send mail
        :param mail_pass: your mailbox password
        :param mail_name: your mailbox nickname
        """
        self.receivers = receivers
        self.mail_host = mail_host  # 设置服务器
        self.mail_user = mail_user
        self.mail_pass = mail_pass
        self.mail_name = mail_user.split("@")[0] if not mail_name else mail_name
        self.me = "".join([self.mail_name, " <", self.mail_user, ">"])

    # to_list：收件人；sub：主题；content：邮件内容
    def _send(self, to_list, sub, content):
        # me = "".join(["SingSam", " <", self.mail_user, ">"])  # 这里的hello可以任意设置，收到信后，将按照设置显示
        msg = MIMEText(content, _subtype='html', _charset='utf-8')  # 创建一个实例，这里设置为html格式邮件
        msg['Subject'] = Header(sub, 'utf-8')  # 设置主题
        msg['From'] = self.me
        msg['To'] = ";".join(to_list)
        try:
            with SMTP_SSL(self.mail_host) as s:
                s.login(self.mail_user, self.mail_pass)  # 登陆服务器
                s.sendmail(self.me, to_list, msg.as_string())  # 发送邮件
            return True
        except Exception as e:
            print(str(e))
            return False

    def send_mail(self, sub, content):
        self._send(self.receivers, sub, content)
