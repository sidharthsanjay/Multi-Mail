import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Your email and app password
sender_email = "example@gmail.com"
password = "xxxxxxxxxxxxx"  # App password with no spaces

# List of recipients
recipient_list = [
    "example@gmail.com"
]

# Subject and body
subject = " "
body = """

text

"""

# Path to your PDF file (resume)
pdf_path = " "

# Sending emails
for recipient in recipient_list:
    # Create message container
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient
    msg["Subject"] = subject

    # Attach body
    msg.attach(MIMEText(body, "plain"))

    # Attach PDF
    with open(pdf_path, "rb") as f:
        part = MIMEApplication(f.read(), Name="example.pdf")
        part["Content-Disposition"] = 'attachment; filename="example.pdf"'
        msg.attach(part)

    # Send email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, recipient, msg.as_string())
        print(f"Email with PDF sent to: {recipient}")
