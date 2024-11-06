# Create_mail

This project generates a temporary email address using the **1secmail** service API. It can check for incoming emails, display them, save the messages to a local file, and delete the temporary email address when needed. Additionally, it includes functionality to send emails through a Gmail account with two-factor authentication (2FA) support.

## Features

- **Generate a random temporary email address** from the available domains.
- **Check for incoming messages** at regular intervals.
- **Save email content** to a local file for offline access.
- **Delete email address** to clear inbox data when the program is terminated.
- **Send email** functionality with logging support, allowing you to send email messages through Gmail (even if you use two-factor authentication).

## Requirements

- Python 3.x
- `requests` library for receiving temporary emails
- `smtplib` and `email` modules (built-in) for sending emails

To install the required library, use:
```bash
pip install requests
