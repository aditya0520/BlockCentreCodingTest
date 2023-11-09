from flask import Flask, request, jsonify, make_response
from flask_cors import CORS, cross_origin
from rpy2 import robjects
from datetime import date 
from fpdf import FPDF
import smtplib, ssl
from email.message import EmailMessage

app = Flask(__name__)
cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
})
app.config['CORS_HEADERS'] = 'Content-Type'


@cross_origin()
@app.route('/add_todo', methods=['POST'])
def add_todo():
    jsonObj = request.get_json()
    firstName = jsonObj["state"]["fname"]
    lastName = jsonObj["state"]["lname"]
    dob = jsonObj["state"]["dob"]
    gender = jsonObj["state"]["gender"]
    email = jsonObj["state"]["email"]
    result = getAgeDay(dob)
    generatePDF ((firstName, lastName, result[0], result[1]))
    sendMail(email)
    print(result[0], result[1])
    return ""

def generatePDF(result):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 15)
    pdf.cell(200, 10, txt = "The Block Centre for Technology and Society", 
         ln = 1, align = 'C')
    pdf.set_font("Arial", size = 12)
    pdf.cell(200, 10, txt = "Name: " + str(result[0]) + " " + str(result[1]),
         ln = 2, align = 'L')
    pdf.cell(200, 10, txt = "Age: " + str(result[2]) + " Years",
         ln = 2, align = 'L')
    pdf.cell(200, 10, txt = "Day of the Week of Birth: " + str(result[3]),
         ln = 2, align = 'L')
    pdf.output("output.pdf")

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


def getAgeDay(dob):
    currentDate = date.today()
    robjects.r('''
    date_diff <- function(x, y) {
        today <- as.Date(x)
        past <- as.Date(y)
        return(round(as.numeric((today - past)/365)))
    }
        day_of_birth <- function(x) {
        return(strftime(as.Date(x), "%A"))
        }
    ''')
    r_f1 = robjects.r['date_diff']
    r_f2 = robjects.r['day_of_birth']

    age = r_f1(str(currentDate),str(dob))
    day = r_f2(str(dob))
    return int(age[0]), day[0]
    

if __name__ == "__main__":
    app.run(port=8000, debug=True)