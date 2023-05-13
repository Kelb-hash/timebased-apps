import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


#Email configuration
sender = "ekusama7@gmail.com"
recepient =  'wkusama7@gmail.com'
password = 'yjzywwbzgrggxjkk'
subject = 'testing app'
message = """

first time testing my python timebased email sender app sending message at 10 seconds intervals

"""

def send_mail():
    #mime Msg create
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recepient
    msg.attach(MIMEText(message, 'plain'))
    
    #connect to SMTP server and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        #server.starttls()
        server.login(sender, password)
        server.send_message(msg)

#send mail every ten second
while True:
    send_mail()
    print('mail succ. sent')
    time.sleep(600)
