
import os
import smtplib

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

        # NOTE: pre-formatted message!
        msg = f'From: From Person {sender}\nTo: {receiver}\nSubject: {subject}\n\n{msg_payload}'

        print(f'\nEmail\n<<<\n{msg}\n>>>\n')
        
        mail_server = smtplib.SMTP(SMTP_HOST)
        mail_server.sendmail(sender, receivers, msg)


    except Exception as e:
        print(f'ERROR: {str(e)}')

if __name__ == '__main__':
    main()