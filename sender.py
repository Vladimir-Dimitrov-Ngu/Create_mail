import logging
import smtplib
from email.mime.text import MIMEText


logging.basicConfig(
    filename="email_sender.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def send_email(from_email, password, subject, body, to_email):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(from_email, password)
            server.sendmail(from_email, to_email, msg.as_string())
        logging.info("Email sent successfully from %s to %s", from_email, to_email)
    except smtplib.SMTPAuthenticationError as e:
        logging.error("Authentication failed for %s: %s", from_email, e)
    except Exception as e:
        logging.error("Failed to send email from %s to %s: %s", from_email, to_email, e)


if __name__ == "__main__":
    from_email = input("Input sender email: ")
    to_email = input("Input email to: ")
    password = input("Input password: ")
    send_email(
        from_email, password, "Test Subject", "This is a test email body.", to_email
    )
