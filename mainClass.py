from wtforms import Form, BooleanField, StringField, validators, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, Length
from flask_wtf import FlaskForm

#==============================================
# DOCTOR FORMS VALIDATOR
#==============================================
class validatorForm(Form):
    Prescription = StringField(' ',
                               [
                                   validators.Required(
                                       message='this field is empty'),
                                   validators.Length(
                                       min=4, max=125, message='this field is empty'),

                               ])
    Referencia = StringField(' ',
                             [
                                 validators.Length(min=4, max=25),
                                 validators.Required(
                                     message='this field is empty')
                             ])
    Note = StringField(' ', [
        validators.Length(min=4, max=25),
        validators.Required(message='this field is empty')
    ])

    # Assign Medication
    assigMed = StringField(' ', [
        validators.Length(min=4, max=25, message='this field is empty'),
        validators.Required()

    ])
    Indications = StringField(' ', [
        validators.Length(min=4, max=25),
        validators.Required(message='this field is empty')

    ])
    # Assign Test
    TestName = StringField(' ', [
        validators.Length(min=4, max=25),
        validators.Required(message='this field is empty')

    ])
    DoBefore = StringField(' ', [

        validators.Length(min=4, max=25),
        validators.Required(message='this field is empty')

    ])

#==============================================
# NURSE FORMS VALIDATOR
#==============================================
class Nourse(Form):
    Diagnosis = StringField(' ',
                               [
                                   validators.Required(
                                       message='this field is empty'),
                                   validators.Length(
                                       min=4, max=125, message='this field is empty'),

                               ])
    Allergies = StringField(' ',
                             [
                                 validators.Length(min=4, max=25),
                                 validators.Required(
                                     message='this field is empty')
                             ])
    Mets = StringField(' ', [
        validators.Length(min=4, max=25),
        validators.Required(message='this field is empty')
    ])

    # Assign Medication
    BldPressure = StringField(' ', [
        validators.Length(min=4, max=25, message='this field is empty'),
        validators.Required()

    ])
    Breathing = StringField(' ', [
        validators.Length(min=4, max=25),
        validators.Required(message='this field is empty')

    ])
    # Assign Test
    Pulse = StringField(' ', [
        validators.Length(min=4, max=25),
        validators.Required(message='this field is empty')

    ])
    BdTemperature = StringField(' ', [

        validators.Length(min=4, max=25),
        validators.Required(message='this field is empty')

    ])

    NrsObservation = StringField(' ', [

        validators.Length(min=4, max=25),
        validators.Required(message='this field is empty')

    ])

    MdlIssues = StringField(' ', [

        validators.Length(min=4, max=25),
        validators.Required(message='this field is empty')

    ])

    InttService = StringField(' ', [

        validators.Length(min=4, max=25),
        validators.Required(message='this field is empty')

    ])

    newFieldtService = StringField(' ', [

        validators.Length(min=4, max=25),
        validators.Required(message='this field is empty')

    ])

    NewFieldIssues = StringField(' ', [

        validators.Length(min=4, max=25),
        validators.Required(message='this field is empty')

    ])

#==============================================
# USER VALIDATOR
#==============================================
class UserLog(Form):
    Username = StringField(' ', validators=[InputRequired(), Length(min=4, max=25)]) 
    Password = StringField(' ', validators=[InputRequired(), Length(min=4, max=25)])

#==============================================
# DoctorList
#==============================================
class DoctorList(Form):
    mkAppoiment = StringField(' ', validators=[InputRequired(), Length(min=4, max=25)])   
    mkAppoimentTime = StringField(' ', validators=[InputRequired(), Length(min=4, max=25)])

#==============================================
# USER REGISTER
#==============================================
class Register(Form):
    firstname = StringField(' ', validators=[InputRequired(), Length(min=4, max=25)]) 
    LastName = StringField(' ', validators=[InputRequired(), Length(min=4, max=25)])
    BOD = StringField(' ', validators=[InputRequired(), Length(min=4, max=25)]) 
    address = StringField(' ', validators=[InputRequired(), Length(min=4, max=25)]) 
    telephone = StringField(' ', validators=[InputRequired(), Length(min=4, max=25)]) 
    email = StringField(' ', validators=[InputRequired(), Length(min=4, max=25)])
    
