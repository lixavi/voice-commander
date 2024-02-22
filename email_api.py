# email_api.py

import smtplib
import imaplib
import email

class EmailAPI:
    def __init__(self, smtp_server, smtp_port, imap_server, imap_port, username, password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.imap_server = imap_server
        self.imap_port = imap_port
        self.username = username
        self.password = password

    def send_email(self, recipient, subject, message):
        try:
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.username, self.password)
            email_message = f"Subject: {subject}\n\n{message}"
            server.sendmail(self.username, recipient, email_message)
            server.quit()
            return "Email sent successfully."
        except Exception as e:
            return f"An error occurred while sending email: {e}"

    def receive_emails(self):
        try:
            server = imaplib.IMAP4_SSL(self.imap_server, self.imap_port)
            server.login(self.username, self.password)
            server.select("inbox")
            _, data = server.search(None, "ALL")
            email_ids = data[0].split()
            emails = []
            for email_id in email_ids:
                _, data = server.fetch(email_id, "(RFC822)")
                raw_email = data[0][1]
                email_message = email.message_from_bytes(raw_email)
                sender = email_message["From"]
                subject = email_message["Subject"]
                body = self.get_email_body(email_message)
                emails.append({"sender": sender, "subject": subject, "body": body})
            server.close()
            server.logout()
            return emails
        except Exception as e:
            return f"An error occurred while receiving emails: {e}"

    def get_email_body(self, email_message):
        if email_message.is_multipart():
            for part in email_message.walk():
                content_type = part.get_content_type()
                if "text/plain" in content_type:
                    return part.get_payload(decode=True).decode()
        else:
            return email_message.get_payload(decode=True).decode()
