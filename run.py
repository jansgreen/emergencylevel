import pymongo
import stripe
import mainClass
import json
import os
from pymongo import MongoClient
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_materialize import Material  
from datetime import datetime, timedelta
from bson.objectid import ObjectId




app = Flask(__name__)
Material(app)

# MONGODB CONNECTION
client = pymongo.MongoClient("mongodb+srv://jansgreen:Lmongogreen07@cluster0-ajilk.mongodb.net/test?retryWrites=true&w=majority")
db = client["userRecord"]
dbColl = db["userRecord"]

# STRIPE API KEY
secreKey = 'sk_test_RTba6nZ1WHPp4rAX65VasJL600Uc7R8pg2'
publicKey = 'pk_test_0p4jqeiFYPzrkeRsn0iQdaSO00VNNlhS7K'
stripe.api_key = secreKey

# SETTING
app.secret_key = 'mysecretkey'
imgFolder = os.path.join('static','img')
app.config['UPLOAD_FOLDER']=imgFolder


@app.route('/')
def index():
    homeImg= os.path.join(app.config['UPLOAD_FOLDER'], 'homeimg.jpg')
    return render_template("index.html", homeImg=homeImg)

@app.route('/patient')
def patient():
    return render_template("patient.html")


@app.route('/PatientScreem')
def PatientScreem():
    return render_template("PatientScreem.html")


@app.route('/ticket/<string:id>')
def ticket(id):
    ticketFullName = dbColl.find({"_id": ObjectId(id)})
    FullTicket = ticketFullName
    now = datetime.now()
    ticketNumData = now.strftime('%d%m%YE%H%M%S')
    dateTicket = now.strftime('%d/%m/%Y %H:%M')
    flash(ticketNumData)
    print(FullTicket)
    Ticketquery = {"_id": ObjectId(id)}
    newvalues = {"$set": {
        "Emergincy."+ticketNumData: {'Date': dateTicket}
    }
    }
    dbColl.update(Ticketquery, newvalues)
    return render_template("ticket.html", FullTickets=FullTicket)


@app.route('/addPatient', methods=['POST'])
def addPatient():
    if request.method == 'POST':
        name = request.form['first_name']
        lastName = request.form['last_name']
        BOD = request.form['BOB']
        Address = request.form['address']
        Email = request.form['email']
        numPhone = request.form['icon_telephone']
        Condition = request.form['condition']
        ntCondition = request.form['ntCondition']
        Category = "Patient"
        dataPost = {
            "Category": Category,
            "FirstName": name,
            "LastName": lastName,
            "BOD": BOD,
            "Address": Address,
            "Email": Email,
            "Phone": numPhone,
            
        }
        condition = {
            "Condition": Condition,
            "Note": ntCondition
        }
    _id = dbColl.insert_one(dataPost)
    TicketID = _id.inserted_id
    dbColl.update({"_id": ObjectId(TicketID)}, {
        '$set': {"MedicalNote":[condition]}
    })
    return redirect(url_for("ticket", id=TicketID))


@app.route('/doctorList')
def doctorList():
    DoctorsList = dbColl.find({'Category': 'staff'}).skip(1).limit(1)
    name = DoctorsList
    return render_template("doctorList.html", Name=name)


@app.route('/pageDoctorList/<int:id>', methods=['GET'])
def pageDoctorList(id):
    PageNum = int(id)
    data = dbColl.find({'Emergincy': {'$exists': 'true'}}
                       ).skip(PageNum).limit(1)
    count = data.count()
    if PageNum == count-1:
        PageNums = PageNum - PageNum
    else:
        PageNums = PageNum + 1
    emergencyTeam()
    return render_template("doctorList.html", datas=data, num=PageNums)


@app.route('/staff')
def staff():
    count = dbColl.count()
    return render_template("staff.html", counts=count,
                           selectPosition=[{'Position': 'Doctor'}, {'Position': 'Nourse'}, {'Position': 'Hosekeeping'}, {'Position': 'Stretcher-bearer'}])


@app.route('/emergencyTeam')
def emergencyTeam():
    TicketsPages = dbColl.find({'Emergincy': {'$exists': 'true'}}).limit(5)
    for TicketsPage in TicketsPages:
        flash(TicketsPage)
        pass
    nums = int(0)
    num = nums
    return render_template("emergencyTeam.html", num=num)


@app.route('/page/<int:id>', methods=['GET'])
def page(id):
    PageNum = int(id)
    data = dbColl.find({'Emergincy': {'$exists': 'true'}}
                       ).skip(PageNum).limit(1)
    count = data.count()
    if PageNum == count-1:
        PageNums = PageNum - PageNum
    else:
        PageNums = PageNum + 1
    emergencyTeam()
    return render_template("emergencyTeam.html", datas=data, num=PageNums)


@app.route('/ticketTurn')
def ticketTurn():
    ticketTurn = dbColl.find({"Emergincy": [1]})
    return render_template("emergencyTeam.html", ticketTurns=ticketTurn)


@app.route('/board')
def board():
    return render_template("board.html")


@app.route('/addStaff', methods=['POST'])
def addStaff():
    if request.method == 'POST':
        name = request.form['first_name'].istittle()
        lastName = request.form['last_name'].istittle()
        BOD = request.form['BOB']
        Address = request.form['address'].istittle()
        Email = request.form['email'].islow()
        numPhone = request.form['icon_telephone']
        language = request.form['language'].istittle()
        Tabnumber = dbColl.count()
        rooms = request.form['rooms']
        Position = request.form.get('Position').istittle()
        Category = "staff"
        dataPost = {
            "Category": Category,
            "FirstName": name,
            "LastName": lastName,
            "BOD": BOD,
            "Address": Address,
            "Email": Email,
            "Phone": numPhone,
            "language": language,
            "Tabnumber": Tabnumber,
            "rooms": rooms,
            "Position": Position
        }
    dbColl.insert_one(dataPost)
    return render_template("staff.html")


@app.route('/room')
def room():
    return render_template("room.html")


@app.route('/Nourse/<string:id>', methods=['POST'])
def Nourse(id):
    Nourse = mainClass.Nourse(request.form)
    if request.method == 'POST'and Nourse.validate():
        AllergiesV = request.form['Mets'],
        MetsV = request.form['BldPressure'],
        DiagnosisV = request.form['Allergies'],
        BldPressureV = request.form['Diagnosis'],
        BreathingV = request.form['Breathing'],
        PulseV = request.form['Pulse'],
        BdTemperatureV = request.form['BdTemperature'],
        NrsObservationV = request.form['NrsObservation'],
        MdlIssuesV = request.form['MdlIssues'],
        InttServiceV = request.form['InttService']
        
        now = datetime.now()
        MedicalDate = now.strftime('Date: %d-%m-%Y Hours: %H:%M:%S')
        try:
            NewFieldIssuesV = request.form['NewFieldIssues'],
            newFieldtServiceV = request.form['newFieldtService'],
            MedicalData={ 
                "Nurse": "Nurse",
                "Diagnosis":DiagnosisV,
                "BloodPressure":BldPressureV,
                "Breathing":BreathingV,
                "Allergies":AllergiesV,
                "Mets":MetsV,
                "Pulse":PulseV,
                "BodyTemperature":BdTemperatureV,
                "NurseObservation":NrsObservationV,
                "MedicalIssues":MdlIssuesV,
                "IntensityService":InttServiceV,
                "OtherIssues":NewFieldIssuesV,
                "OtherService":newFieldtServiceV,
                "Date": MedicalDate,
                  }
            pass
        except:
             MedicalData={ 
                "Breathing":BreathingV,
                "Allergies":AllergiesV,
                "Mets":MetsV,
                "Pulse":PulseV,
                "BodyTemperature":BdTemperatureV,
                "NurseObservation":NrsObservationV,
                "MedicalIssues":MdlIssuesV,
                "IntensityService":InttServiceV,
                "OtherIssues":NewFieldIssuesV,
                "OtherService":newFieldtServiceV,
                "Date": MedicalDate,
                  }
        finally:
            dbColl.update({"_id": ObjectId(id)}, {
                '$push': {'MedicalNote':[MedicalData]}})
            pass



        Pressure = request.form['Pressure'],
        weight = request.form['weight'],
        VitalSigns = request.form['VitalSigns'],
        Note = request.form['Note']
        MedicalData = {"Pressure": Pressure, "weight": weight,
                       "VitalSigns": VitalSigns, "Note": Note}
    now = datetime.now()
    MedicalDate = now.strftime('Date: %d-%m-%Y Hours: %H:%M:%S')
    dbColl.update({"_id": ObjectId(id)}, {
                  '$set': {"MedicalNote."+MedicalDate: {"Nourse": MedicalData}}})
    return redirect(url_for("emergencyTeam"))


@app.route('/addNourse/<string:id>')
def addNourse(id):
    DrPasientsID = id
    NourseForm = mainClass.Nourse(request.form)
    patientData = dbColl.find({'_id': ObjectId(DrPasientsID)})
    return render_template("/Nourse.html", PatientId=patientData, DrPasientID=DrPasientsID, form=NourseForm)


@app.route('/Doctor/<string:id>', methods=['POST'])
def Doctor(id):
    validatorForms = mainClass.validatorForm(request.form)
    if request.method == 'POST' and validatorForms.validate():
        Prescription = request.form['Prescription'],
        Referencia = request.form['Referencia'],
        Note = request.form['Note']
        AssigMed = request.form['assigMed'],
        Indications = request.form['Indications'],
        TestName = request.form['TestName'],
        DoBefore = request.form['DoBefore'],
        now = datetime.now()
        MedicalDate = now.strftime('Date: %d-%m-%Y Hours: %H:%M:%S')
        try:
            newMed = request.form['newMed'],
            newInd = request.form['newInd'],
            readyTestName = request.form['readyTestName'],
            readyDoBefore = request.form['readyDoBefore'],
            MedicalData={ 
                "Doctor": "DoctorName",
               "Prescription": Prescription,
               "Referencia": Referencia,
               "Note": Note,
               "Medication": (AssigMed, Indications),
               "OtherMedication":(newMed, newInd),
               "Test": (TestName, DoBefore),
               "OtherTest":(readyTestName,readyDoBefore),
               "MedicalDate":MedicalDate
                  }
            pass
        except:
             MedicalData={ 
                "Doctor": "DoctorName",
               "Prescription": Prescription,
               "Referencia": Referencia,
               "Note": Note,
               "Medication": (AssigMed, Indications),
               "Test": (TestName, DoBefore),
               "MedicalDate":MedicalDate
                  }
        finally:
            dbColl.update({"_id": ObjectId(id)}, {
                '$push': {'MedicalNote':[MedicalData]}})
            pass

    return redirect(url_for("emergencyTeam"))


@app.route('/addDoctor/<string:id>')
def addDoctor(id):
    DrPasientsID = id
    validatorForms = mainClass.validatorForm(request.form)
    patientData = dbColl.find({'_id': ObjectId(id)})
    return render_template("/Doctor.html", DrPasientID=DrPasientsID, patientsData=patientData, form=validatorForms)


@app.route('/Seach', methods=['POST'])
def Seach():
    if request.method == 'POST':
        PatientSeachD = request.form['Patientseach']
        PatientData = dbColl.find(
            {'Email': PatientSeachD, 'Category': 'Patient'})
        PatientDataOuts = PatientData
    return render_template("PatientScreem.html", PatientDataOut=PatientDataOuts)


@app.route('/facture')
def facture():
    return render_template("/facture.html", publicKeys=publicKey)


@app.route('/session', methods=['POST'])
def session():
    print(request.form)
    Crecustomer = stripe.Customer.create(
        email=request.form['stripeEmail'], source=request.form['stripeToken'])
    chargeData = stripe.Charge.create(
        customer=Crecustomer.id,
        amount=9.99,
        currency='usd',
        description='The Producto'
    )
    print(chargeData)
    return render_template("/facture.html")


if __name__ == '__main__':
    app.run(port=5500, debug=True)
