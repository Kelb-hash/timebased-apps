import smtplib
import time
from email.mime.text import MIMEText
#from email.mime.multipart import MIMEMultipart


#Email configuration
sender = "ekusama7@gmail.com"
recepients =  ['wkusama7@gmail.com', 'joynnamani088@gmail.com', 'wkusamahr@gmail.com']
password = 'yjzywwbzgrggxjkk'
subject = 'testing app'
message = """

first time testing my python timebased email sender app sending message at 10 seconds intervals, i love you Ogechukwu

"""

def send_mail():
    #mime Msg create
    
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ','.join(recepients)
    
    
    #connect to SMTP server and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        #server.starttls()
        server.login(sender, password)
        #loop into recepient for multiple mails
    

        server.send_message(msg)
        print("mail succ. sent to ")

#send mail every ten second
while True:
    send_mail()
    time.sleep(600)
