import pymongo
from pymongo import MongoClient
from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
from datetime import timedelta
from flask_material import Material
from bson.objectid import ObjectId


app = Flask(__name__)
Material(app)

# MONGODB CONNECTION
client = pymongo.MongoClient(
    "mongodb+srv://jansgreen:Lmongogreen07@cluster0-ajilk.mongodb.net/test?retryWrites=true&w=majority")
db = client["userRecord"]
dbColl = db["userRecord"]


# SETTING
app.secret_key = 'mysecretkey'


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/patient')
def patient():
    return render_template("patient.html")

@app.route('/PatientScreem')
def PatientScreem():
    return render_template("PatientScreem.html")


@app.route('/ticket')
def ticket():
    return render_template("ticket.html")


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
            "Condition": Condition,
            "Note": ntCondition
        }
    dbColl.insert_one(dataPost)
    now = datetime.now()
    ticketNum = now.strftime('%d%m%YE%H%M%S')
    flash(ticketNum)
    fullName= name+" "+lastName
    flash(fullName)
    return redirect(url_for("ticket"))


@app.route('/doctorList')
def doctorList():
    DoctorsList = dbColl.find({'Category': 'staff'})
    name = DoctorsList
    return render_template("doctorList.html", Name = name)


@app.route('/staff')
def staff():
    count = dbColl.count()
    return render_template("staff.html", counts =count,
                           selectPosition=[{'Position': 'Doctor'}, {'Position': 'Nourse'}, {'Position': 'Hosekeeping'}, {'Position': 'Stretcher-bearer'}])


@app.route('/emergencyTeam')
def emergencyTeam():
    PatientsList = dbColl.find({'Category': 'Patient'})
    patientListDB = PatientsList
    return render_template("emergencyTeam.html", PatientList = patientListDB, DoctorNote=[{'Pressure': "<input>"}, {'weight': '<input>'}, {'stability': '<input>'}])


@app.route('/board')
def board():
    return render_template("board.html")


@app.route('/addStaff', methods=['POST'])
def addStaff():
    if request.method == 'POST':
        name = request.form['first_name']
        lastName = request.form['last_name']
        BOD = request.form['BOB']
        Address = request.form['address']
        Email = request.form['email']
        numPhone = request.form['icon_telephone']
        language = request.form['language']
        Tabnumber = dbColl.count()
        rooms = request.form['rooms']  # request.form.to_dict() USALO PARA ASIGNAR PERSONAL A LOS ROOMS
        Position = request.form.get('Position')
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
    if request.method == 'POST':
        Pressure = request.form['Pressure'],
        weight = request.form['weight'],
        VitalSigns = request.form['VitalSigns'],
        Note = request.form['Note']
        MedicalData = {"Pressure": Pressure, "weight": weight, "VitalSigns": VitalSigns, "Note": Note} 
    now = datetime.now()
    MedicalDate = now.strftime('Date: %d-%m-%Y Hours: %H:%M:%S')
    dbColl.update({"_id":ObjectId(id)}, {'$set': {"MedicalNote."+MedicalDate:{"Nourse":MedicalData}}})
    return redirect(url_for("emergencyTeam"))

@app.route('/addNourse/<string:id>')
def addNourse(id):
    PatientsID = id
    return render_template("/Nourse.html", PatientId = PatientsID)

@app.route('/Doctor/<string:id>', methods=['POST'])
def Doctor(id):
    if request.method == 'POST':
        Prescription = request.form['Prescription'],
        Referencia = request.form['Referencia'],
        Note = request.form['Note']
    MedicalData = {"Prescription": Prescription, "Referencia": Referencia, "Note": Note} 
    now = datetime.now()
    MedicalDate = now.strftime('Date: %d-%m-%Y Hours: %H:%M:%S')
    dbColl.update({"_id":ObjectId(id)}, {'$set': {"MedicalNote."+MedicalDate:{"Doctor":MedicalData}}})
    return redirect(url_for("emergencyTeam"))

@app.route('/addDoctor/<string:id>')
def addDoctor(id):
    DrPasientsID = id
    return render_template("/Doctor.html", DrPasientID = DrPasientsID)




if __name__ == '__main__':
    app.run(port=5500, debug=True)
