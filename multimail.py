import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Your email and app password
sender_email = "sidsidsapkaal@gmail.com"
password = "mhrgossublprlusl"  # App password with no spaces

# List of recipients
recipient_list = [
    "CV@Arabianfal.com",
    "Cv@aldawaa.com.sa",
    "Hr.qrm@hotmail.com",
    "Rec@alojaimi.com",
    "Recruitment@rawabiholding.com",
    "Job.s6@hotmail.com",
    "Careers@dnata.com",
    "Hr@alesayi_motors.com",
    "Hr@alarayan.com",
    "Recruiting.ksa@mcmermott.com",
    "Recruitment@aytb.com",
    "Wadaef@gtecorp.com",
    "Careers@nesr.com",
    "Recruit@farm.com.sa",
    "Info@alhumamlaw.com",
    "Hr1@gulfteksaudi.com",
    "Catcosa@catcosa.com",
    "Cv@tafear.com",
    "Recruitment@sraco.com.sa",
    "Career@sidco.com.sa",
    "Info@atco.com.sa",
    "HRdepartmental@sa.yokogawa.com",
    "Recruitment@shadeco.com",
    "Klc.hr@alkafaa.com",
    "Kbr-amcdehr@kbr.com",
    "Recruitment@batook.com",
    "Career@shawarmer.com",
    "Hrsupport@archirodon.net",
    "Jobs@binajinah.com",
    "Marketing.np@nesma.com",
    "Wadaef2019@abdulla-fouad.com",
    "Careers@innosoft.sa",
    "M@startime.com.sa",
    "job@musk.sa.com",
    "Shababwatansa@gmail.com",
    "j@sabksa.com",
    "al.alshaikh@bonyan.sa",
    "ymohammed@innovest.com.sa",
    "al.alshaikh@bonyan.sa",
    "s.alwadi@nhc.sa",
    "i.atassi@artar.com.sa",
    "oalkhunaizi@darwaemaar.com",
    "jobs@almasah.net",
    "recruitment.amjad@gmail.com",
    "jobrydlaw@gmail.com",
    "Job@almoosahospital.com.sa",
    "recruitment@almoosahospital.com.sa",
    "jobs@sghgroup.net",
    "career.dmm@sghgroup.net",
    "talent.acquisition@drsulaimanalhabib.com",
    "Careers@jhah.com",
    "hrd@alahsahospital.com.sa",
    "career@almanahospital.com.sa",
    "info@familycare.com.sa",
    "info@ramclinics.com",
    "HR.DSFHR@fakeeh.care",
    "career@mouwasat.com",
    "careers@dallah-hospital.com",
    "hr.phc@drsulaimanalhabib.com",
    "careers@almurjanhospital.com",
    "hiringnow.ksa@gmail.com",
    "recruitment@wecareksa.com"
]

# Subject and body
subject = "Application for Data Analyst Role – Sidharth Sapkaal"
body = """
Dear Hiring Manager,

I hope this message finds you well.

I am writing to express my interest in the Data Analyst position at your esteemed organization. With a B.Tech in Computer Science Engineering and practical experience in data analytics, visualization, and automation, I am confident in my ability to contribute meaningfully to your data-driven team.

During my internships at PropMarker and Quest Innovative Solutions, I developed and deployed Power BI dashboards, automated reporting pipelines using Python, and worked extensively with SQL, Excel, and MongoDB. I also led initiatives in predictive modeling and ETL development, enabling actionable insights across operations and sales workflows. My hands-on experience with Excel (advanced formulas, pivot tables), Power BI, and data storytelling directly aligns with the responsibilities outlined for this role.

I am passionate about turning data into strategic decisions and continuously seek opportunities to optimize business processes through analytical insights. My project portfolio further reflects my ability to integrate tools like Streamlit, AWS S3, and machine learning frameworks to build real-time, interactive analytics solutions.

Please find my resume attached for your review. I would welcome the opportunity to discuss how my background and skills can contribute to your team’s success.

Thank you for considering my application. I look forward to the possibility of speaking with you further.

Warm regards,
Sidharth Sanjay Sapkaal
+91 7034605066
sidsidsapkaal@gmail.com
https://www.linkedin.com/in/sidharthsapkaal/
"""

# Path to your PDF file (resume)
pdf_path = "C:\\Users\\sidsi\\OneDrive\\Desktop\\Sid\\SIDHARTH_SAPKAAL.pdf"

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
        part = MIMEApplication(f.read(), Name="SIDHARTH_SAPKAAL.pdf")
        part["Content-Disposition"] = 'attachment; filename="SIDHARTH_SAPKAAL.pdf"'
        msg.attach(part)

    # Send email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, recipient, msg.as_string())
        print(f"✅ Email with PDF sent to: {recipient}")
