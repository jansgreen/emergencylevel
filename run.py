import pymongo
import stripe
import mainClass
import json
import os
import bcrypt
import smtplib 
from pymongo import MongoClient
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_materialize import Material  
from datetime import datetime, timedelta
from bson.objectid import ObjectId
from flask_pymongo import PyMongo  



app = Flask(__name__)
Material(app)

# MONGODB CONNECTION
client = os.environ.get('MONGODB_URI')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI', 'mongodb://localhost')
dbColl = PyMongo(app)


# SETTING 
app.secret_key = 'mysecretkey'
imgFolder = os.path.join('static','img')
app.config['UPLOAD_FOLDER']=imgFolder

#dbColl = os.environ.get('dbColl')
#print(dbColl)

@app.route('/')
def index():
    homeImg= os.path.join(app.config['UPLOAD_FOLDER'], 'homeimg.jpg')
    if 'Username' in session:
        pass
    return render_template("index.html", homeImg=homeImg)

#======================================================================================= PATIENT AREA

@app.route('/testing')
def testing():
    mainLog()
    print(mainLog.id())
    return redirect(url_for('board'))


@app.route("/logout")
def logout():
    if 'Username' in session:
        session.pop('Username', None)
        return redirect(url_for('index'))

@app.route('/PatientScreem')
def PatientScreem():
    UserLog = mainClass.UserLog(request.form)
    Seach = mainClass.Seach(request.form)
    PatientDataOut =[]
    return render_template("PatientScreem.html", form=UserLog, Seach=Seach, PatientDataOut = PatientDataOut)

@app.route('/PatientRegister')
def PatientRegister():
    Seach = mainClass.Seach(request.form)
    Register = mainClass.Register(request.form)
    visit = {
        "Category":"Patient",
        "FirstName": "name",
        "userAccount": " ",
        }
    _id = dbColl.insert_one(visit)
    id = _id.inserted_id    
    return render_template("register.html", form=Register, seach=Seach, id = id)

@app.route('/register/<string:id>', methods = ['GET'])
def register(id):
    Seach = mainClass.AllSeach(request.form)
    Register = mainClass.Register(request.form)
    user = dbColl.find_one({'_id':ObjectId(id)})
    if user:
        if user['Category']== 'DirectorDoctor':
            Category = user['Category']
            flash(" ",Category)
            return render_template("register.html", form=Register, seach=Seach, id = id)
        elif user['Category']== 'Patient':
            return render_template("register.html", form=Register, id = id)
    else:
        return render_template("register.html", form=Register, id = id)
    return render_template("index.html")

@app.route('/addRegister/<string:id>', methods = ['GET', 'POST'])
def addRegister(id):
    Register = mainClass.Register(request.form)
    if request.method == 'POST' and Register.validate:
        name = request.form['firstname']
        lastName = request.form['LastName']
        BOD = request.form['BOD']
        Address = request.form['address']
        Email = request.form['email']
        numPhone = request.form['telephone']
        if 'Username' in session:
            Userdata = dbColl.find_one({'_id':ObjectId(id)})
            print("Profundidad 1")
            print(Userdata)
            if Userdata:
                print(Userdata)
                Category = Userdata['Category']
                print("Profundidad 2")
                print(Userdata)
                if Category=="DirectorDoctor":
                    print("Profundidad 3")
                    print(Userdata)
                    New_Category = request.form['SeachSelect']
                    specialty = request.form['specialty']
                    dataPost = {
                        "Category": New_Category,
                        "FirstName": name,
                        "LastName": lastName,
                        "BOD": BOD,
                        "Address": Address,
                        "Email": Email,
                        "Phone": numPhone,
                        "userAccount": " ",
                        "Specialty"   : specialty
                        
                    }
                    _id = dbColl.insert_one(dataPost)
                    id = _id.inserted_id
                    if id: 
                        return redirect(url_for("AutoEmail", id=id))
        else:
            _id = dbColl.update({"_id":ObjectId(id)}, {'$set':{"FirstName": name, "LastName": lastName, "BOD": BOD, "Address": Address, "Email": Email, "Phone": numPhone }})
            patientId = id
            if patientId:
                return redirect(url_for("ticket", id=patientId))
    return redirect(url_for("board", id=id))

        

#=============================================================================================================================
# API 
#=============================================================================================================================
@app.route('/AutoEmail/<string:id>') 
def AutoEmail(id):
    for user in dbColl.find({'_id': ObjectId(id)}):
        pass
        patienFirstName = user['FirstName']
        patienLastName = user['LastName']
        patienEmail = user['Email']
        patienCategory = user['Category']
    if patienFirstName:
        if patienCategory == "Patient":
            EmailMessage = patienFirstName+" "+patienLastName+" We have information that you have registered at the emergency level, if you have been your favor, visit the following url to continue with the registration process. "+'https://emergencylevel.herokuapp.com/singup/'+id
            subject= 'Emergency, Continue your singup'
            Email = 'Subject: {}\n\n{}'.format(subject, EmailMessage)
            EmailSystem = smtplib.SMTP('smtp.gmail.com', 587)
            EmailSystem.starttls()
            EmailSystem.login('emergencylebel@gmail.com', 'Lemergencylebel07')
            EmailSystem.sendmail('emergencylebel@gmail.com', patienEmail, Email)
            EmailSystem.quit()
            return redirect(url_for("index"))
        else:
            EmailMessage = patienFirstName +" "+patienLastName+" We have information that you have registered at the emergency level, if you have been your favor, visit the following url to continue with the registration process. "+'https://emergencylevel.herokuapp.com/singup/'+id
            subject= 'Emergency, Continue your singup'
            Email = 'Subject: {}\n\n{}'.format(subject, EmailMessage)
            EmailSystem = smtplib.SMTP('smtp.gmail.com', 587)
            EmailSystem.starttls()
            EmailSystem.login('emergencylebel@gmail.com', 'Lemergencylebel07')
            EmailSystem.sendmail('emergencylebel@gmail.com', patienEmail, Email)
            EmailSystem.quit()
            return redirect(url_for("redirecting"))
    return redirect(url_for("index"))

@app.route('/redirecting', methods=['GET','POST'])
def redirecting():
    UserLog = mainClass.UserLog(request.form)
    if 'Username' in session:
        UserName = session['Username']
        userLog = dbColl.find_one({'userAccount.UserName': UserName})
        id = userLog['_id']
        print(id)
        if userLog:
            session['Username'] = UserName
            Category = userLog['Category']
            id = userLog['_id']
            flash(" ", Category)
            return redirect(url_for("board", id =id ) )
        else:
            print('Error')
    else:
        print('Usuario no encontrado')
    return redirect(url_for("index"))



#======================================================================================= GENERATOR TICKET
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
#======================================================================================= EMPLOYEE AREA
#========================================================= DOCTOR AREA

@app.route('/about')
def room():
    return render_template("doctorList.html")

@app.route('/staff')
def staff():
    if 'Username' in session:
        StaffTeam = mainClass.UserLog(request.form)
        return render_template("staff.html", form=StaffTeam)
    else:
        StaffTeam = mainClass.UserLog(request.form)
        return render_template("staff.html", form=StaffTeam)

@app.route('/board/<string:id>')
def board(id):
    if 'Username' in session:
        datadb = dbColl.find_one({"_id":ObjectId(id)})
        if datadb:
           Category = datadb['Category']
           flash(" ",Category)
        return render_template("board.html", id = id, data = datadb)
    else:
        print("You are not user register")
        return redirect(url_for("index"))
    return render_template("board.html", id = id)


#========================================================= EMERGENCY AREA
@app.route('/EmergencyStaff/<string:id>')
def EmergencyStaff(id):
    if 'Username' in session:
        staff = dbColl.find_one({'_id':ObjectId(id)})
        page_size = 1
        page_num = 1
        skips = page_size * (page_num - 1)
        pages = dbColl.find({'Emergincy': {'$exists': 'true'}}).skip(skips).limit(page_size)
        for page in pages:
            print(page)
            pass
        if staff:
            patientListBD = dbColl.find({'Emergincy': {'$exists': 'true'}}).limit(5)
            if staff['Category'] == 'Nurse':
                Category = staff['Category']
                flash(" ", Category)
                return render_template("emergencyTeam.html", data=staff, ListBD = patientListBD, num=page, id=id )
            elif staff['Category'] == 'Doctor':
                Category = staff['Category']
                flash(" ", Category)
                return render_template("emergencyTeam.html", data=staff, ListBD = patientListBD, num=page, id=id)
            elif staff['Category'] == 'DirectorDoctor':
                Category = staff['Category']
                flash(" ", Category)
                return render_template("emergencyTeam.html", data=staff, ListBD = patientListBD, num=page, id=id)
            else:
                print("hubo un error usted no esta autorizado a esta area")
                return redirect(url_for("index"))
    return redirect(url_for("index"))


#========================================================= Login AREA
@app.route('/singup/<string:id>')
def singup(id):
    Register = mainClass.UserLog(request.form)
    return render_template("singup.html", form = Register, id= id)

@app.route('/addsingup/<string:id>', methods = ['POST'])
def addsingup(id):
    Register = mainClass.UserLog(request.form)
    if request.method == 'POST' and Register.validate:
        newUser = request.form['Username']
        password = request.form['Password']
        CheckUser = dbColl.find_one({'userAccount.UserName': newUser})
        if CheckUser:
            if CheckUser == newUser:
                return redirect(url_for("singup", id = id))  
            else:  
                dbColl.update({'_id': ObjectId(id)}, {
                        '$set': {'userAccount':{"UserName":newUser, "Password":password}}})
                session['Username']= request.form['Username'] 
                return redirect(url_for("board", id = id))    
    return redirect(url_for("board", id = id))    


@app.route('/mainLog', methods=['GET','POST'])
def mainLog():
    UserLog = mainClass.UserLog(request.form)
    if request.method == 'POST' and UserLog.validate:
        UserName = request.form['Username']
        PassUser = request.form['Password']
        userLog = dbColl.find_one({'userAccount.UserName': UserName})
        PassDb = userLog['userAccount']['Password']
         
        if userLog:
            print(PassDb)
            if PassDb == PassUser:
                session['Username'] = request.form['Username']
                Category = userLog['Category']
                id = userLog['_id']
                FirstName = userLog['FirstName']
                print(FirstName)
                print(id)
                flash(" ", Category)
                return redirect(url_for("board", id =id ) )
            else:
                print('Error')
        else:
            print('Usuario no encontrado')
    return render_template("staff.html", form=UserLog )


#========================================================= Nurse STAFF AREA

@app.route('/Nourse/<string:Cid>/<string:id>', methods=['POST'])
def Nourse(Cid, id):
    if 'Username' in session:
        Nourse = mainClass.Nourse(request.form)
        if request.method == 'POST'and Nourse.validate():
            DrInfo = dbColl.find_one({"_id": ObjectId(Cid)})
            AllergiesV = request.form['Mets']
            MetsV = request.form['BldPressure']
            DiagnosisV = request.form['Allergies']
            BldPressureV = request.form['Diagnosis']
            BreathingV = request.form['Breathing']
            PulseV = request.form['Pulse']
            BdTemperatureV = request.form['BdTemperature']
            NrsObservationV = request.form['NrsObservation']
            MdlIssuesV = request.form['MdlIssues']
            InttServiceV = request.form['InttService']
            
            now = datetime.now()
            MedicalDate = now.strftime('Date: %d-%m-%Y Hours: %H:%M:%S')
            try:
                NewFieldIssuesV = request.form['NewFieldIssues'],
                newFieldtServiceV = request.form['newFieldtService'],
                MedicalData={
                    "Date" : MedicalDate, 
                    "Nurse": DrInfo,
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
                    "Date" : MedicalDate, 
                    "Nurse": DrInfo,
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
                checkedField = dbColl.find_one({"_id": ObjectId(id)})
                print("Escribiendo documentos")
                if checkedField:
                    if "NurseNote":
                        dbColl.update_one({"_id": ObjectId(id)}, {'$push':  {'NurseNote':MedicalData}})
                        print("eL CAMPO MedicalNote EXISTE")
                        return redirect(url_for('EmergencyStaff', id = Cid))
                    else:
                        dbColl.update_one({"_id": ObjectId(id)}, {'$set': {'NurseNote':MedicalData}})
                        print("El campo MedicalNote no existe y fue creado")
                        return redirect(url_for("EmergencyStaff", id=Cid))
    return redirect(url_for("emergencyTeam"))


@app.route('/addNourse/<string:id>')
def addNourse(id):
    if 'Username' in session:
        DrPasientsID = id
        NourseForm = mainClass.Nourse(request.form)
        patientData = dbColl.find({'_id': ObjectId(DrPasientsID)})
    return render_template("/Nourse.html", PatientId=patientData, DrPasientID=DrPasientsID, form=NourseForm)

#========================================================= DOCTOR STAFF AREA

@app.route('/Doctor/<string:Cid>/<string:id>', methods=['POST'])
def Doctor(Cid, id):
    if 'Username' in session:
        DrInfo = dbColl.find_one({"_id": ObjectId(Cid)})
        validatorForms = mainClass.validatorForm(request.form)
        if request.method == 'POST' and validatorForms.validate:
            Prescription = request.form['Prescription'],
            Referencia = request.form['Referencia'],
            Note = request.form['Note'],
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
                    "Date" : MedicalDate, 
                    "Doctor": DrInfo,
                "Prescription": Prescription,
                "Referencia": Referencia,
                "Note": Note,
                "Medication": (AssigMed, Indications),
                "OtherMedication":(newMed, newInd),
                "Test": (TestName, DoBefore),
                "OtherTest":(readyTestName,readyDoBefore),
                "MedicalDate":MedicalDate
                    }
            except:
                MedicalData={ 
                     "Date" : MedicalDate, 
                    "Doctor": DrInfo,
                "Prescription": Prescription,
                "Referencia": Referencia,
                "Note": Note,
                "Medication": (AssigMed, Indications),
                "Test": (TestName, DoBefore),
                    }
            finally:
                checkedField = dbColl.find_one({"_id": ObjectId(id)})
                print("Escribiendo documentos")
                if checkedField:
                    if "DoctorNote":
                        dbColl.update_one({"_id": ObjectId(id)}, {'$push':{'DoctorNote':MedicalData}})
                        print("eL CAMPO MedicalNote EXISTE")
                        return redirect(url_for('EmergencyStaff', id = Cid))
                    else:
                        dbColl.update_one({"_id": ObjectId(id)}, {'$set': {'DoctorNote':MedicalData}})
                        print("El campo MedicalNote no existe y fue creado")
                        return redirect(url_for("EmergencyStaff", id=Cid))
    return redirect(url_for("EmergencyStaff", id=Cid))




@app.route('/addDoctor/<string:idD>/<string:id>', methods = ['GET'])
def addDoctor(idD, id):
    if 'Username' in session:
        validatorForms = mainClass.validatorForm(request.form)
        DrPasientsID = dbColl.find_one({'_id': ObjectId(idD)})
        if DrPasientsID:
            if DrPasientsID['Category'] == 'Doctor':
                Category = DrPasientsID['Category']
                flash(" ", Category)
                patientData = dbColl.find_one({'_id': ObjectId(id)})
                return render_template("/Doctor.html", DrPasientID=DrPasientsID, patientsData=patientData, id=patientData, form=validatorForms)
            elif DrPasientsID['Category'] == 'Nurse':
                Category = DrPasientsID['Category']
                flash(" ", Category)
                patientData = dbColl.find_one({'_id': ObjectId(id)})
                return render_template("/Doctor.html", DrPasientID=DrPasientsID, patientsData=patientData, id=patientData, form=validatorForms)

            elif DrPasientsID['Category'] == 'DirectorDoctor':
                Category = DrPasientsID['Category']
                flash(" ", Category)
                patientData = dbColl.find_one({'_id': ObjectId(id)})
                return render_template("/Doctor.html", DrPasientID=DrPasientsID, patientsData=patientData, id=patientData, form=validatorForms)
            else:
                print('Usted no tiene acceso aqui, hubo un error')
                return redirect(url_for("index"))
        else:
            print('No se encontro la informacion de quien requiere')
            return redirect(url_for("index"))
            
#============================================================================================== Seach  AREA

@app.route('/Seach', methods=['POST'])
def Seach():
    UserLog = mainClass.UserLog(request.form)
    Seach = mainClass.Seach(request.form)
    if request.method == 'POST' and Seach.validate:
        PatientSeachD = request.form['Seach']
        PatientData = dbColl.find_one(
            {'Email': PatientSeachD, 'Category': 'Patient'})
        if PatientData:
            if PatientData['Email'] == PatientSeachD:
                return render_template("PatientScreem.html", PatientDataOut=PatientData, form=UserLog, Seach=Seach)            
        return render_template("PatientScreem.html", PatientDataOut=PatientData, form=UserLog, Seach=Seach)


#==============================================================================================
# BOARD  AREA
#==============================================================================================


#========================================================= Nurse STAFF AREA

@app.route('/SeeAll/<string:id>', methods = ['GET', 'POST'])
def SeeAll(id):
    if 'Username' in session:
        seach = mainClass.AllSeach(request.form)
    return render_template("/SeeAll.html", seach=seach, id=id)

@app.route('/See/<string:id>', methods = ['GET', 'POST'])
def See(id):
    if 'Username' in session:
        seach = mainClass.AllSeach(request.form)
        if request.method=='POST' and seach.validate:
            showData = request.form['SeachSelect']
            userid = dbColl.find_one({'_id':ObjectId(id)})
            if userid:
                if userid['Category']=='Patient' and showData == 'Patient':
                    Category = userid['Category']
                    flash(" ", Category )
                    print("usted no tiene permiso para ver a todos los"+showData)
                    return render_template("/SeeAll.html", seach=seach, AlluserCat=[], id=id)
                elif userid['Category']=='Patient':
                    data= dbColl.find({'Category':showData})
                    Category = userid['Category']
                    flash(" ", Category )
                    return render_template("/SeeAll.html", seach=seach, AlluserCat=data, id=id)
                else:
                    data= dbColl.find({'Category':showData})
                    Category = userid['Category']
                    flash(" ", Category )
                    return render_template("/SeeAll.html", seach=seach, AlluserCat=data, id=id)
            else:
                print("Hubo un error comuniquese con soporte tecnico")
                return redirect(url_for('/index'))
        else:
            print("Seleccione una opcion")
        return render_template("/SeeAll.html", seach=seach, AlluserCat=[], id=id)

#======================================================================================= USER AREA

@app.route('/edit/<string:id>', methods = ['GET', 'POST'])
def edit(id):
    UserLog = mainClass.UserLog(request.form)
    if 'Username' in session:
        AllSeach = mainClass.AllSeach(request.form)
        Register = mainClass.Register(request.form)
        UserName = session['Username']
        userLog = dbColl.find_one({'userAccount.UserName': UserName})
        if userLog:
            session['Username'] = UserName
            Category = userLog['Category']
            flash(" ", Category)
        return render_template("edit.html", seach = AllSeach, form=Register, id = id,)


@app.route('/sumit_edit/<string:id>', methods = ['GET', 'POST'])
def sumit_edit(id):
    UserLog = mainClass.UserLog(request.form)
    Register = mainClass.Register(request.form)
    if 'Username' in session:
        if request.method == 'POST' and Register.validate:
            name = request.form['firstname']
            lastName = request.form['LastName']
            BOD = request.form['BOD']
            Address = request.form['address']
            Email = request.form['email']
            numPhone = request.form['telephone']
            Category = request.form['SeachSelect']
            specialty = request.form['specialty']
            dataPost = {
                "Category": Category,
                "FirstName": name,
                "LastName": lastName,
                "BOD": BOD,
                "Address": Address,
                "Email": Email,
                "Phone": numPhone,
                "Specialty"   : specialty
            }
            dbColl.update({"_id":ObjectId(id)}, {'$set': dataPost})
        UserName = session['Username']
        userLog = dbColl.find_one({'userAccount.UserName': UserName})
        if userLog:
            session['Username'] = UserName
            Category = userLog['Category']
            AdmId = userLog['_id']
            flash(" ", Category)
            return redirect(url_for("board", id =AdmId ) )
        else:
            print('Error')
    else:
        return redirect(url_for("index") )

        
@app.route('/MyDoctor/<string:id>', methods = ['GET', 'POST'])
def MyDoctor(id):
    if 'Username' in session:
        myInfo = dbColl.find_one({"_id": ObjectId(id)})
        return render_template("myDoctors.html", AlluserCat = myInfo, id = id,)

@app.route('/setMyDoctor/<string:id>/<string:Drid>')
def setMyDoctor(id, Drid):
    if 'Username' in session:
        getDoctor = dbColl.find_one({"_id":ObjectId(id)})
        myInfo = dbColl.find_one({"_id":ObjectId(Drid)})
        if getDoctor and myInfo:
            dbColl.update({"_id":ObjectId(Drid)}, {'$set':{'myDoctors':getDoctor}})
            return redirect(url_for('board', id=Drid))
        else:
            DrMessage = "We not have any doctor"
            flash(DrMessage)
        return redirect(url_for('board', id=Drid))

@app.route('/delete/<string:myid>')
def delete(myid):
    if 'Username' in session:
        dbColl.update({"_id":ObjectId(myid)}, {'$unset':{'myDoctors':{'$exists':'true'}}})
        pass
    return redirect(url_for('board', id=myid)) 

@app.route('/deleteDoc/<string:myid>')
def deleteDoc(myid):
    UserLog = mainClass.UserLog(request.form)
    if 'Username' in session:
        dbColl.delete_one({"_id":ObjectId(myid)})
        UserName = session['Username']
        userLog = dbColl.find_one({'userAccount.UserName': UserName})
        if userLog:
            session['Username'] = UserName
            Category = userLog['Category']
            AdmId = userLog['_id']
            flash(" ", Category)
            return redirect(url_for("board", id =AdmId ) )
        else:
            print('Error')
    else:
        return redirect(url_for("index") )
        
@app.route('/myProfile/<string:id>')
def myProfile(id):
    if 'Username' in session:
        Profile = dbColl.find_one({'_id': ObjectId(id)})
        if Profile:
            return render_template("/myProfile.html", Profile = Profile, id=id)
        return render_template("/myProfile.html", Profile = Profile, id=id)



if __name__ == '__main__':
    app.run(port=5500, debug=True)
