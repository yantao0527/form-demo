import os
from smtplib import SMTP_SSL, SMTP_SSL_PORT
from email.mime.multipart import MIMEMultipart, MIMEBase
from email.mime.text import MIMEText
from email.encoders import encode_base64

SMTP_SERVER = os.environ.get("SMTP_SERVER")
SMTP_USERNAME = os.environ.get("SMTP_USERNAME")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")

def send_email(to_email, subject, text_part, files=[]):
    from_email = 'No Reply <no_reply@digitalwas.de>'  # or simply the email address
    to_emails = [to_email]

    # Create multipart MIME email
    email_message = MIMEMultipart()
    email_message.add_header('To', ', '.join(to_emails))
    email_message.add_header('From', from_email)
    email_message.add_header('Subject', subject)
    # email_message.add_header('X-Priority', '1')  # Urgent/High priority

    # Create text and HTML bodies for email
    text_part = MIMEText(text_part, 'plain')
    # html_part = MIMEText('<html><body><h1>HTML!</h1><p>Hello world html text!</p></body></html>', 'html')

    # Attach all the parts to the Multipart MIME email
    email_message.attach(text_part)
    # email_message.attach(html_part)

    for filename, filecontent in files:
        # Create file attachment
        attachment = MIMEBase("application", "octet-stream")
        attachment.set_payload(filecontent)  # Raw attachment data
        encode_base64(attachment)
        attachment.add_header("Content-Disposition", "attachment; filename=" + filename)

        email_message.attach(attachment)

    # Connect, authenticate, and send mail
    smtp_server = SMTP_SSL(SMTP_SERVER, port=SMTP_SSL_PORT)
    # smtp_server.set_debuglevel(1)  # Show SMTP server interactions
    smtp_server.login(SMTP_USERNAME, SMTP_PASSWORD)
    smtp_server.sendmail(from_email, to_emails, email_message.as_bytes())

    # Disconnect
    smtp_server.quit()
