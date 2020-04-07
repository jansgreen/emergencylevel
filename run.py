import pymongo
from pymongo import MongoClient
from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
from datetime import timedelta
from flask_material import Material


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
            "First Name": name,
            "Last Name": lastName,
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
    flash("Name: " + name +" "+lastName)
    return redirect(url_for("ticket"))


@app.route('/doctorList')
def doctorList():
    DoctorsList = dbColl.find({"Category":"staff"})
    for DRlistDB in DoctorsList:
        flash(DRlistDB['First Name'] +" "+ DRlistDB['Last Name']+ " " + DRlistDB['BOD'] +" "+ DRlistDB['Email']+ " " + DRlistDB['Phone']+ " " + DRlistDB['language'] + " "+ DRlistDB['Position'] +" "+ DRlistDB['Tab number'])
    return render_template("doctorList.html")

@app.route('/staff')
def staff():
    return render_template("staff.html")


@app.route('/emergencyTeam')
def emergencyTeam():
     return render_template("emergencyTeam.html")



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
        Tabnumber = request.form.get_json('TabDoctors')
        rooms = request.form['rooms']
        Position = request.form('Position')  #request.form.to_dict() USALO PARA ASIGNAR PERSONAL A LOS ROOMS
        Category = "staff"
        dataPost = {
            "Category": Category,
            "First Name": name,
            "Last Name": lastName,
            "BOD": BOD,
            "Address": Address,
            "Email": Email,
            "Phone": numPhone,
            "language":language,
            "Tab number": Tabnumber,
            "rooms": rooms,
            "Position": Position
        }
    dbColl.insert_one(dataPost)
    return render_template("staff.html")


@app.route('/room')
def room():
    return render_template("room.html")


if __name__ == '__main__':
    app.run(port=5500, debug=True)
