# send emails with python
# using smtplib

import smtplib, ssl

smtp_server = 'smtp.gmail.com'
port = 465

sender = 'xxxxxxxx@gmail.com'
password = input('Enter your password here:')

receiver = 'xxxxxxxxx@gmail.com'
message = """\
from: {}
to: {}
subject: Hello!

I sent this email using python code not by actually opening gmail from browser! That's so cool isn't it??

""".format(sender, receiver)

context = ssl.create_default_context()

# with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#     server.login(sender, password)
#     print('It Worked!')

# try:
#     server = smtplib.SMTP(smtp_server, port)
#     server.ehlo()
#     server.starttls(context=context)
#     server.ehlo()
#     server.login(sender, password)
#     print("It worked!")
# except Exception as e:
#     print(e)
# finally:
#     server.quit()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender, password)

    # send email
    server.sendmail(sender, receiver, message)
