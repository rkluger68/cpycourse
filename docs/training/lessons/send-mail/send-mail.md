!!! question "Lesson: Email-4-You"

    === "Task"

        Send yourself an Email
        
        On program-start ask, the user to provide

        - MAILHOST
        - Email DOMAINNAME

        Afterwards

        - get the username from the shell enivronment variable 'USERNAME' (Windows) or 'USER' (Linux) to prepare your email-address
        - create a connection to the mail-host
        - send yourself an email with the subject "Hello from the Python-Course" and the content = "Currently working on ..." from a synthetic email sender-address e.g. "test.test@foo.de" 


        ``` python
        >>> name = 'Ada'
        ```

        Expected result: Check your email-account for the incoming email

    === "Hints"

        - use `input()`-builtin function to get user informations
        - use `os.environ`- mapping object from the Python Standard Library, to read environment variables
        - use `smtplib.SMTP`- class from the [smtplib](https://docs.python.org/3/library/smtplib.html) module of the Python Standard Library, to establish a connection to the mailserver
        - use f-string `msg = f'From: {sender}\nTo: {receiver}\nSubject: {subject}\n\n{payload}'`

    === "Solution"

        ??? Example - Compact simple Python Email client

            ``` python title="sendmail_compact.py"
            --8<-- "training/lessons/send-mail/sendmail_compact.py"
            ```

            [:material-file-download:](sendmail_compact.py)

            Such simple snippets typically also work well as shell one-liners:

            ``` console title="sendmail-compact.sh"
            --8<-- "training/lessons/send-mail/sendmail-compact.sh"
            ```
            
            ``` ps1con title="sendmail-compact.ps1"
            --8<-- "training/lessons/send-mail/sendmail-compact.ps1"
            ```

        ??? Example - Simple Python Email client using 'MailServer'-class

            ``` python title="sendmail.py"
            --8<-- "training/lessons/send-mail/sendmail.py"
            ```

            [:material-file-download:](sendmail.py)

            Such simple snippets typically also work well as shell one-liners:

            ``` console title="sendmail.sh"
            --8<-- "training/lessons/send-mail/sendmail.sh"
            ```
            
            ``` ps1con title="sendmail.ps1"
            --8<-- "training/lessons/send-mail/sendmail.ps1"
            ```


        ??? Example - Python Email client sending attachments

            ``` python title="sendmail_with_attachment.py"
            --8<-- "training/lessons/send-mail/sendmail_with_attachment.py"
            ```

            [:material-file-download:](sendmail_with_attachment.py)

