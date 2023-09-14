
import os
import smtplib
import sys

class MailServer:
    def __init__(self, smtp_host):
        self.mailserver = smtplib.SMTP(smtp_host)
        #self.mailserver.set_debuglevel(1)
           
    def __del__(self):
        if self.mailserver:
            self.mailserver.quit()

    def send_mail(self, sender, receivers, msg):
        ''' send a pre-formatted' message '''
        self.mailserver.sendmail(sender, receivers, msg)


def main():
    try:
        # Ask for mail-server
        SMTP_HOST = input("SMTP_HOST: ")
        domain_name = input("E-MAIL DOMAINNAME: ")

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
       
        print(f'\nEmail\n<<<\n{msg}\n>>>\n')
        
        mailServer= MailServer(SMTP_HOST)
        # # Provide a pre-formatted message 'msg'
        mailServer.send_mail(sender, receivers, msg)

    except Exception as e:
        print(f'ERROR: {str(e)}')

if __name__ == '__main__':
    main()