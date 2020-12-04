# Emergencylevel

[open in heroku](https://emergencylevel.herokuapp.com/):

emergency level is an application that seeks to manage the information of patients who enter the emergency room by generating a number of tickets to speed up the quality of care, the interns will be able to complete their information in liena or the nurse will be able to fill in the missing data.

the Director Doctor has access to delete, add and modify the information of the doctors.

This consists of a dashboard, where the user will have access to seven functions depending on their category, the Intern will only be able to do a search, see their information and select and / or see the main doctor.

The doctors, will be able to access Emergencyteam, here they will be able to attend to the patients who leave by registering in emergencylevel and they will be able to carry a report of the patient per day.

External API (smtp.gmail.com) This has an API that uses the email of the app and sends the user a link to complete the user information and password.

this application is made with the programming languages ​​HTML, CSS, JavaScript, Python + Flask and the design is based on materialcss, and it has a Json format database in mongodb and hosted in heroku

## The Director Doctor you can test
# Demo Director Doctor
- UserName: Jansgreen
- Password: L123456789
    * Only the ManagerDoctor can add and delate other Doctor and Nurse.

# Demo Doctor
- Username: XelohimGreen
- Password: L123456789
# Demo Nurse (all nurse can be add by Director Doctro)
- Username: xewisgreen
- Password: X123456789
# Demo Patient
- you can create the patient

# Design
    - Colour Scheme
        Three colors predominate: fuchsia pink, light blue and white, the buttons of some functions have a bluish green fill.
# Typography
    - https://fonts.googleapis.com/css?family=Roboto:400,700, We have used this font because we want to create the environment in which information is being used and data is being dealt with.
# Icons
    We using the icons of Material in the foother, to give a better graphical display to the user

# Imagery
    We have placed an image in each of the following paragraphs that we show on the frontend of our website, to illustrate the message to each of our patients.
    1. Index
        - Cut the waiting time
        - Pregnant women should receive the right care at the right time.
        - When consumers choose health care
    2. I'm Employee
        - We Work
        - We are the hospital of the future
        - QUALITY CARE BEGINS WITH QUALITY PEOPLE

    3. About
        - Organizational and Functional Levels
        - Mission and Vision.
        - Institutional values

# Heroku
- Create a user on heroku at https://www.heroku.com/, create the application and assign it a name "Emergency Level"; Once my application is ready, create the variables
* These are the variables in the heroku settings:

**Access_key**: This is the variable that stores the access key that we use for mongodb connection.

**User_key**: This is the variable that stores the username in mongo db, in combination with the Access_key plus the link (mongodb + srv: // "+ s1_handler +": "+ s2_handler +" @ cluster0-ajilk.mongodb.net / test ? retryWrites = true & w = majority), makes connection to mongodb Atlas possible.

**GMAIL_EMAIL**: this is the variable that saves the sender's email, for sending mail to emails, which we use to create the username and password through the unique link.
     
**GMAIL_PASS**: Like GMAIL_EMAIL, this variable saves the sender's email password, this is the password for Gmail applications.

**SECRET_KEY**: This is the variable that my python secret key has.

* Buildpacks
heroku / python (with this I specify to heroku that the programming language I will use is python)

After having configured the variables, I created my procfile (Procfile) file in my local application with the following web configuration: gunicorn run: app, thus telling heroku to run the gunicorn server for this application. and then download Heroku CLI.
as I had already done git init in the folder of my application and within it I did the following steps to deploy in Heroku:
      $ heroku login
      $ heroku git: remote -an emergency level
      git add.
      git commit -m "implement in heroku"
      git push heroku master



# Testing 
1. main.css; I uploaded my main.css file to jigsaw.w3.org and did the validation test.    

    <p>we used W3C for test all css code in this project
<a href="http://jigsaw.w3.org/css-validator/check/referer">
    <img style="border:0;width:88px;height:31px"
        src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
        alt="¡CSS Válido!" />
    </a>
</p>

I loaded each of the HTML files located in the templates directory at [validator.w3.org](https://validator.w3.org/#validate_by_upload), to validate it

2. Flask unittest, We using the FlaskTest, to test (in the terminal writhe python test.py to see the test) all template html and python code, in the file test.py

# Defensive Design
  Flask-Toastr: shows a message to the user, accessible to the categories of flask, Error, info, warning and success 


##  The CRUD Operations Work

* The [Mongodb](https://cloud.mongodb.com/v2/): we are usin the Mongo database Atlas, we are using the Mongo database system, to store user data; where it can create, update, read, delete, at will.

## how do we apply this?
The regular patient in [MyDoctor](https://emergencylevel.herokuapp.com/MyDoctor): The User can add the doctor he wants, he can read the information about the doctors that he has in his profile, he can eliminate any doctor from his list.

Then when the user creates, the user creates her account in our application and also when she creates a ticket for the waiting shift in the emergency room.

Only with these conditions we have complied with The CRUD Operations Work.

**C**: The in the tab I'm patient; the patient can Create a database, in the option Register, it is a form with the patient data and afther it will print a Tickets.
![Screenshot](readmeImg/createCRUD.png)

**R**: In the Options My Doctor/Add a Doctor, the patient can choose and read informations about doctor and nurse.
![Screenshot](readmeImg/readCRUD.png)

**U**: In this area the patient can READ and UPDATE from mongodb, when the user clic in ADD THIS DOCTOR.
it is posible in MyDoctor option, clic in Add a Doctor and select a Doctor options and clic CHOOSE; for other options the patient can only read.
![Screenshot](readmeImg/updateCRUD.png)

**D**: In MyDoctor the patient can READ and DELETE the doctorNote Field. and My account you can delete a record from mongodb, Delete my Account

![Screenshot](readmeImg/deleteCRUD2.png)

![Screenshot](readmeImg/deleteCRUD.png)



## Library used
 * Flask 1.1.2: flask a library especially for small applications like this, although this app seems to be powerful. the flask library allows us to use Jinja2==2.11.2 to have data communication enter the server with python and html.

 * Flask-WTF 0.14.3: allows us to have a better handling of the forms and a better visualization of it.

 * Pymongo 3.11.1: Is a Python library to connect to a MongoDB database.
 
 * bcrypt 3.2.0: Is a library that allows you to encrypt sensitive data so that it cannot be interpreted by a third party

 * Gunicorn: Is to serve all the dynamics of a project on a server. and in this application we use it for Heroku.

 * python-decouple: like the os library, this allows us to extract data from a external file in our environment, we apply it to sensitive information.

## Lenguage Used
- HTML
- Javascripts
- Cascading Style Sheets -CSS
- Python 3.7.7

## Template base
- Materialize. Availible at [github](https://github.com/Dogfalo/materialize):


## materialcss
https://materializecss.com/
Materialize. Availible at https://github.com/Dogfalo/materialize
Flask-Materialize. Available at https://bitbucket.org/cyberspy/flask_materialize

## Youtube
https://www.youtube.com/watch?v=3ZS7LEH_XBg
https://www.youtube.com/watch?v=4o7C4JMGLe4&t=374s
https://www.youtube.com/watch?v=iIhAfX4iek0&t=239s
