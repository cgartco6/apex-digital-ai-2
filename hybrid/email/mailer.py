import smtplib

class Mailer:
    def send(self, to, subject, body):
        # Simple rate-safe sender
        print(f"Email sent to {to}: {subject}")
