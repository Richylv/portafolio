import smtplib, ssl


def send_mail(message):
    host = "smtp.gmail.com"
    port = 465
    password = "kdnbapnyivqdwejh"
    username = "draftherlv@gmail.com"
    receiver = "draftherlv@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
