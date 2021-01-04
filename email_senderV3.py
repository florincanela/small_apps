from email.message import EmailMessage
import smtplib
from pathlib import Path
from string import Template

money = '1,000,000$'
name = ''
msg = EmailMessage()
html = Template(Path('index.html').read_text())

msg['Subject'] = f'You Won {money}!!!'
msg['To'] = ""
msg['From'] = f'Loteria Romana'

msg.set_content(html.substitute({'money': money, 'name': name}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as s:
    s.ehlo()
    s.starttls()
    s.login('', '')
    s.send_message(msg)