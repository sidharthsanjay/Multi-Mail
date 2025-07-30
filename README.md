# Multi-Mail
Automated Personalized Email Sender with PDF Attachment

This Python script automates the process of sending individual emails with a custom subject, body text, and a PDF attachment to a large list of hiring contacts. Each recipient receives a personalized message without seeing other recipients, ensuring privacy and compliance with professional standards.

✅ Key Features:
Secure Login using Gmail SMTP (smtplib.SMTP_SSL) and App Password authentication.

Recipient Privacy: Sends emails one-by-one, so recipients do not see others (unlike CC/BCC).

MIME Support: Uses MIMEMultipart to include both plain text and PDF attachments.

Attachment Handling: Attaches the resume file (SIDHARTH_SAPKAAL.pdf) securely in each email.

Loop-Based Dispatch: Iterates through the recipient list and sends emails in a loop with progress logs.

📂 Files Involved:
example.pdf: Resume file located locally, attached to each email.

🛡️ Security Note:
The password used is a Gmail App Password, not the actual Gmail account password, to enhance security and comply with Google's email policy.

It's strongly recommended to store credentials securely using environment variables or encrypted secrets instead of hardcoding in production.

🛠️ Dependencies:
smtplib

email.mime modules (MIMEMultipart, MIMEText, MIMEApplication)
