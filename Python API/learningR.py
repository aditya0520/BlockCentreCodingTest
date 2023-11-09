from rpy2 import robjects
from datetime import date 
from dateutil.relativedelta import relativedelta 
import smtplib, ssl
from email.message import EmailMessage
def sendMail(email):

	msg = EmailMessage()
	msg["Subject"] = "RA Position - The Block Centre for Technology and Society"
	msg["From"] = "aditya.ayush5520@gmail.com"
	msg["To"] = email
	with open("output.pdf","rb") as f:
		msg.add_attachment(
			f.read(),
			filename="output.pdf",
			maintype="application",
			subtype="pdf"
        )

	context=ssl._create_unverified_context()

	with smtplib.SMTP("smtp.gmail.com", port=587) as smtp:
		smtp.starttls(context=context)
		smtp.login(msg["From"], "lrqc hwpu yhap jaie")
		smtp.send_message(msg)

sendMail("affare@gmail.com")
currentDate = date.today()
pastDate = date.today() -  relativedelta(years = 5) 


# print(str(currentDate))
# print(str(pastDate))

# print(r_f(str(currentDate),str(pastDate)))
# print(r_f1(str(pastDate)))


    # with open("attachment.zip", "rb") as f:
    #     msg.add_attachment(
    #         f.read(),
    #         filename="attachment.zip",
    #         maintype="application",
    #         subtype="zip"
    #     )