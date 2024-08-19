
import smtplib
import logging
from email.message import EmailMessage
import os
import mimetypes



class EMAIL:

    #To send multiple email pas in to_email as a list of strings
    #

    def __init__(self, EMAIL_PASS, from_email, to_email, subject, content_string, attachment_one_path=None, attachment_two_path=None):
        self.EMAIL_PASS = EMAIL_PASS
        self.from_email = from_email
        self.to_email = to_email
        self.subject = subject
        self.content_string = content_string
        self.attachment_one_path = attachment_one_path
        self.attachment_two_path = attachment_two_path



    def add_attachment(self, msg, attachment_path):
        if attachment_path:
            attachment_name = os.path.basename(attachment_path)
            ctype, encoding = mimetypes.guess_type(attachment_path)

            if ctype is None or encoding is not None:
                ctype = 'application/octet-stream'
            maintype, subtype = ctype.split('/', 1)

            with open(attachment_path, 'rb') as attachment:
                msg.add_attachment(attachment.read(),
                                    maintype=maintype,
                                    subtype=subtype,
                                    filename=attachment_name)



    def send(self):

        #Insert to_email as a list if sending to multiple email addresses

        msg = EmailMessage()
        msg['Subject'] = self.subject
        msg['From'] = self.from_email
        msg['To'] = self.to_email
        msg.set_content(self.content_string)

         # Add attachments if they exist
        self.add_attachment(msg, self.attachment_one_path)
        self.add_attachment(msg, self.attachment_two_path)


        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            try:
                smtp.login(self.from_email, self.EMAIL_PASS)
                logging.info('Succesfully logged into GMAIL')
            except Exception as e:
                logging.error(f'Unable to login due to error {e}')
            
            try:
                smtp.send_message(msg)
                logging.info(f'Succesfully sent message via GMAIL account {self.from_email}')
            except Exception as e:
                logging.error(f'Unable to send emails due to error {e}')




# msg = EmailMessage()
# msg['Subject'] = 'PowerSchool Email Notification'
# msg['From'] = EMAIL_ADDRESS
# msg['To'] = ['samuel.taylor@greendot.org']
# msg.set_content('Email containing daily logs')