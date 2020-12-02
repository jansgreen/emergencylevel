from run import app
import unittest


class FlaskTestCase(unittest.TestCase):

    #Testin the login 
    def test_index_login(self):
        test = app.test_client(self)
        response = test.get('/mainLog', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    
    #Testin the logout
    def test_index_patient(self):
        test = app.test_client(self)
        response = test.get('/PatientScreem', content_type='html/text')
        self.assertEqual(response.status_code, 200)

        #Testin the index
    def test_index(self):
        test = app.test_client(self)
        response = test.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

        #Testin the PatientRegister
    def test_index_PatientRegister(self): 
        test = app.test_client(self)
        response = test.get('/PatientRegister', content_type='html/text')
        self.assertEqual(response.status_code, 200)

        #Testin the about
    def test_index_about(self):
        test = app.test_client(self)
        response = test.get('/about', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        
        #Testin the staff
    def test_index_staff(self):
        test = app.test_client(self)
        response = test.get('/staff', content_type='html/text')
        self.assertEqual(response.status_code, 200)

        #Testin the register
    def test_index_register(self):
        test = app.test_client(self)
        response = test.get('/register/5ec950782c626e45e172b538', content_type='html/text')
        self.assertEqual(response.status_code, 200)

        
        #Testin the addRegister
        # it return 302 because the user id is ready exits
    def test_index_addRegister(self):
        test = app.test_client(self)
        response = test.get('/addRegister/5ec950782c626e45e172b538', content_type='html/text')
        self.assertEqual(response.status_code, 302)


        #Testin the AutoEmail
    def test_index_AutoEmail(self):
        test = app.test_client(self)
        response = test.get('/AutoEmail/5ec950782c626e45e172b538', content_type='html/text')
        self.assertEqual(response.status_code, 302)

        #Testin the ticket
    def test_index_ticket(self):
        test = app.test_client(self)
        response = test.get('/ticket/5ec950782c626e45e172b538', content_type='html/text')
        self.assertEqual(response.status_code, 200)

        #Testin the board
        # this test return 302, because need login before go to board
    def test_index_board(self):
        test = app.test_client(self)
        response = test.get('/board/5ec950782c626e45e172b538', content_type='html/text')
        self.assertEqual(response.status_code, 302)

if __name__ == "__main__":
    unittest.main()
