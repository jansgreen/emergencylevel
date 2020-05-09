from wtforms import Form, BooleanField, StringField, PasswordField, validators



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

