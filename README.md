# sendmail

## Example
```
receivers = ["XXXX@126.com"]
mail_host = "smtp.163.com"
mail_user = "XXXX@163.com"
mail_pass = "XXXXXXX"
mail = Mail(receivers, mail_host, mail_user, mail_pass)
context = "".join(["There are some context", str(datetime.datetime.now())])
mail.send_mail("This is sub", context)
```
