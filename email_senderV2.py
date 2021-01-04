from email.message import EmailMessage
import smtplib



msg = EmailMessage()
with open('txt.txt') as txt:
    msg.set_content(txt.read())

msg['Subject'] = 
msg['To'] = 
msg['From'] = 


with smtplib.SMTP(host='smtp.gmail.com', port=587) as s:
    s.ehlo()
    s.starttls()
    s.login()
    for i in range(1):
        s.send_message(msg)
        print(f'sent {i+1}/100')

