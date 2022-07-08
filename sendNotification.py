import smtplib
from email.mime.text import MIMEText

def send(titel, email_text):
    msg = MIMEText(email_text)
    sender = "pascal.klamroth@gmail.com"
    # Gmail Daten
    gmail_user=sender
    gmail_password="behcpbznscmjmlus"

    empfaenger = sender

    msg['Subject'] = titel
    msg['From'] = sender
    msg['To'] = empfaenger

    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(gmail_user, gmail_password)
    smtp_server.sendmail(sender, empfaenger, msg.as_string())
    smtp_server.quit()
    print("Benachrichtigung versendet.")