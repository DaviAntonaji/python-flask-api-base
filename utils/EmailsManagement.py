import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

class EmailsManagement:

    def sendEmail(self, _from, to, subject, message):
        SMTP_EMAIL = os.getenv("SMTP_EMAIL")
        SMTP_SERVER = os.getenv("SMTP_SERVER")
        SMTP_PORT = int(os.getenv("SMTP_PORT"))
        SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = _from
        msg["To"] = to

        text = "Use um navegador compatível com HTML5"
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(message, "html")
        msg.attach(part1)
        msg.attach(part2)

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_EMAIL, SMTP_PASSWORD)
            server.sendmail(_from, to, msg.as_string().encode("latin1"))

        server.quit()
