
from email.message import EmailMessage
import os
import smtplib, sys, time


class MailServer:
    def __init__(self, smtp_host):
        self.mail_server_name = smtp_host
        self.mailserver = smtplib.SMTP(smtp_host)
        #self.mailserver.set_debuglevel(1)
           
    def __del__(self):
        if self.mailserver:
            self.mailserver.quit()

    def send_mail(self, sender, receivers, msg):
        ''' send a pre-formatted' message '''
        self.mailserver.sendmail(sender, receivers, msg)

    def send_mail_with_attachment(self, sender, receivers, subject, payload, filename):
        ''' send mail with attachment, build message using EmailMessage'''
        # https://docs.python.org/3/library/email.examples.html

        # Prepare message
        email = EmailMessage()
        email['Subject'] = subject
        email['From'] = sender
        email['To'] = ','.join(receivers)
        email.set_content(payload)
        with open(filename, 'rb') as fp:
            img_data = fp.read()
        email.add_attachment(img_data, maintype='image', subtype='png',
            filename=os.path.basename(filename))
 
        self.mailserver.send_message(email)

def main():
    try:
        # Ask for mail-server
        SMTP_HOST = input("SMTP_HOST: ")
        domain_name = input("E-MAIL DOMAINNAME: ")
        filename = input("ATTACHMENT-FILE: ")

        if os.name == 'nt':
            user = os.environ['USERNAME']
        elif os.name == 'posix':
            user = os.environ['USER']

        sender = 'test.test@foo.de'
        subject = 'Python-Course Test SMTP-Email'
        msg_payload= 'This is a test Email.'
        receiver = f"{user}@{domain_name}" 
        receivers = [receiver] # must be a list

        # NOTE: Need this special format! see help()
        msg = f'From: From Person {sender}\nTo: {receiver}\nSubject: {subject}\n\n{msg_payload}'
       
        mailServer= MailServer(SMTP_HOST)

        # # Provide a pre-formatted message 'msg'
        mailServer.send_mail(sender, receivers, msg)
        # Generate the message inside the send_mail_2() using payload
        mailServer.send_mail_with_attachment(sender, receivers, subject, msg_payload, filename)

    except Exception as e:
        print(f'ERROR: {str(e)}')

if __name__ == '__main__':
    main()