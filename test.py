# Imports needed
import os
from flask_pymongo import PyMongo
from app import app
import unittest


# Import my env.py that's ignored by git
if os.path.exists("env.py"):
    import env


# Set usernames and passwords for login tests
USERNAME_ADMIN = os.environ.get('USERNAME_ADMIN')
USERNAME_USER = os.environ.get('USERNAME_USER')
SPW_ONE = os.environ.get('SPW_ONE')
SPW_TWO = os.environ.get('SPW_TWO')


# MongoDB configuration
mongo = PyMongo(app)
vacancy = mongo.db.vacancies.find_one()
candidate_user = mongo.db.candidates.find_one({'user_name': USERNAME_USER})
candidate_admin = mongo.db.candidates.find_one({'user_name': USERNAME_ADMIN})
application = mongo.db.applications.find_one()


VACANCY_ID = vacancy['_id']
CANDIDATE_ID_USER = candidate_user['_id']
CANDIDATE_ID_ADMIN = candidate_admin['_id']
APPLICATION_ID = application['_id']


class RoutesVisitorAvailable(unittest.TestCase):
    '''
    testClass for all routes for a visitor of the site
    which are available for a visitor
    '''

    # Ensure that route opens contact page
    def test_contact(self):
        tester = app.test_client()
        response = tester.get(
            '/contact',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 200)

    # Ensure that route opens index page
    def test_index(self):
        tester = app.test_client()
        response = tester.get(
            '/index',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 200)

    # Ensure that route opens login page
    def test_login(self):
        tester = app.test_client()
        response = tester.get(
            '/login',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 200)

    # Ensure that route opens register page
    def test_register(self):
        tester = app.test_client()
        response = tester.get(
            '/register',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 200)

    # Ensure that route opens vacancies page
    def test_vacancies(self):
        tester = app.test_client()
        response = tester.get(
            '/vacancies',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 200)


class RoutesVisitorUnavailable(unittest.TestCase):
    '''
    testClass for all routes/views for a visitor of the site
    which are unavailable for a visitor
    '''
    # Ensure that a visitor gets the message that this page cannot be found
    def test_addapplicationFromVacancie(self):
        tester = app.test_client()
        response = tester.get(
            '/add_application/abcdefg',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 404)

    # Ensure that a visitor gets the message that this page cannot be found
    def test_addapplicationFromApplicationPage(self):
        tester = app.test_client()
        response = tester.get(
            '/add_application/admin',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 404)

    # Ensure that a visitor gets the message that this page cannot be found
    def test_addapplicationFromApplicationPageId(self):
        tester = app.test_client()
        response = tester.get(
            f'/add_application/{VACANCY_ID}',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 404)

    # Ensure that a visitor gets the message that this page cannot be found
    def test_adduser(self):
        tester = app.test_client()
        response = tester.get(
            '/add_user',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 404)

    # Ensure that a visitor gets the message that this page cannot be found
    def test_addvacancy(self):
        tester = app.test_client()
        response = tester.get(
            '/add_vacancy',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 404)

    # Ensure that a visitor gets the message that this page cannot be found
    def test_applications(self):
        tester = app.test_client()
        response = tester.get(
            '/applications',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 404)

    # Ensure that a visitor gets the message that this page cannot be found
    def test_myapplications(self):
        tester = app.test_client()
        response = tester.get(
            '/myapplications',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 500)

    # Ensure that a visitor gets the message that this page cannot be found
    def test_changepassword(self):
        tester = app.test_client()
        response = tester.get(
            '/change_password/abcdefg',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 404)

    # Ensure that a visitor gets the message that this page cannot be found
    def test_changepasswordId(self):
        tester = app.test_client()
        response = tester.get(
            f'/change_password/{CANDIDATE_ID_USER}',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 404)

    # Ensure that a visitor gets the message that this page cannot be found
    def test_changepasswordRandomId(self):
        tester = app.test_client()
        response = tester.get(
            '/change_password/abcdef',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 404)

    # Ensure that a visitor gets the message that this page cannot be found
    def test_editapplicationId(self):
        tester = app.test_client()
        response = tester.get(
            f'/edit_application/{APPLICATION_ID}',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 404)

    # Ensure that a visitor gets the message that this page cannot be found
    def test_editapplication(self):
        tester = app.test_client()
        response = tester.get(
            '/edit_application',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 404)

    # Ensure that a visitor gets the message that this page cannot be found
    def test_editapplicationRandomId(self):
        tester = app.test_client()
        response = tester.get(
            '/edit_application/abcdef',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 404)

    # Ensure that a visitor gets the message that this page cannot be found
    def test_edituser(self):
        tester = app.test_client()
        response = tester.get(
            '/edit_user',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 404)

    # Ensure that a visitor gets the message that this page cannot be found
    def test_edituserId(self):
        tester = app.test_client()
        response = tester.get(
            f'/edit_password/{CANDIDATE_ID_USER}',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 404)

    # Ensure that a visitor gets the message that this page cannot be found
    def test_edituserRandomId(self):
        tester = app.test_client()
        response = tester.get(
            '/edit_user/abcdef',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 404)

    # Ensure that a visitor gets the message that this page cannot be found
    def test_editvacancy(self):
        tester = app.test_client()
        response = tester.get(
            '/edit_vacancy',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 404)

    # Ensure that a visitor gets the message that this page cannot be found
    def test_editvacancyId(self):
        tester = app.test_client()
        response = tester.get(
            f'/edit_vacancy/{VACANCY_ID}',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 404)

    # Ensure that a visitor gets the message that this page cannot be found
    def test_editvacancyRandomId(self):
        tester = app.test_client()
        response = tester.get(
            '/edit_vacancy/abcdef',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 404)

    # Ensure that a visitor gets the message that this page cannot be found
    def test_profile(self):
        tester = app.test_client()
        response = tester.get(
            '/profile',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 404)

    # Ensure that a visitor gets the message that this page cannot be found
    def test_profileId(self):
        tester = app.test_client()
        response = tester.get(
            f'/profile/{CANDIDATE_ID_USER}',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 404)

    # Ensure that a visitor gets the message that this page cannot be found
    def test_profileRandomId(self):
        tester = app.test_client()
        response = tester.get(
            '/profile/adbcdef',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 404)

    # Ensure that a visitor gets the message that this page cannot be found
    def test_users(self):
        tester = app.test_client()
        response = tester.get(
            '/users',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 404)


class loadsVisitorAvailable(unittest.TestCase):
    '''
    testClass for all page loads for a visitor of the site
    which are available for a visitor
    '''

    # Ensure that the contact page loads correctly
    def test_contact_loads(self):
        tester = app.test_client()
        response = tester.get(
            '/contact',
            content_type='html/text'
        )
        self.assertTrue(b'<h1>Contact Us</h1>' in response.data)

    # Ensure that the index page loads correctly
    def test_index_loads(self):
        tester = app.test_client()
        response = tester.get(
            '/index',
            content_type='html/text'
        )
        self.assertTrue(b'<h1>Welcome to BOS UP</h1>' in response.data)

    # Ensure that the login page loads correctly
    def test_login_loads(self):
        tester = app.test_client()
        response = tester.get(
            '/login',
            content_type='html/text'
        )
        self.assertTrue(b'<h1>Login Page</h1>' in response.data)

    # Ensure that the register page loads correctly
    def test_register_loads(self):
        tester = app.test_client()
        response = tester.get(
            '/register',
            content_type='html/text'
        )
        self.assertTrue(b'<h1>Registration</h1>' in response.data)

    # Ensure that the vacancies page loads correctly
    def test_vacancies_loads(self):
        tester = app.test_client()
        response = tester.get(
            '/vacancies',
            content_type='html/text'
        )
        self.assertTrue(b'<h1>Open Vacancies</h1>' in response.data)


class loadsVisitorUnvailable(unittest.TestCase):
    '''
    testClass for all page loads for a visitor of the site
    which are unavailable for a visitor
    '''
    # Ensure that the error page loads correctly
    def test_addapplicationId_loads(self):
        tester = app.test_client()
        response = tester.get(
            f'/add_application/{VACANCY_ID}',
            content_type='html/text'
        )
        self.assertTrue(b'<h1>404 Seems you got lost</h1>' in response.data)

    # Ensure that the error page loads correctly
    def test_addapplication_loads(self):
        tester = app.test_client()
        response = tester.get(
            '/add_application/',
            content_type='html/text'
        )
        self.assertTrue(b'<h1>404 Seems you got lost</h1>' in response.data)

    # Ensure that the error page loads correctly
    def test_addapplicationRandomId_loads(self):
        tester = app.test_client()
        response = tester.get(
            '/add_application/abcdefg',
            content_type='html/text'
        )
        self.assertTrue(b'<h1>404 Seems you got lost</h1>' in response.data)

    # Ensure that the error page loads correctly
    def test_addapplicationFromApplicationPage(self):
        tester = app.test_client()
        response = tester.get(
            '/add_application/admin',
            content_type='html/text'
        )
        self.assertTrue(b'<h1>404 Seems you got lost</h1>' in response.data)

    # Ensure that the error page loads correctly
    def test_adduser(self):
        tester = app.test_client()
        response = tester.get(
            '/add_user',
            content_type='html/text'
        )
        self.assertTrue(b'<h1>404 Seems you got lost</h1>' in response.data)

    # Ensure that the error page loads correctly
    def test_addvacancy(self):
        tester = app.test_client()
        response = tester.get(
            '/add_vacancy',
            content_type='html/text'
        )
        self.assertTrue(b'<h1>404 Seems you got lost</h1>' in response.data)

    # Ensure that the error page loads correctly
    def test_applications(self):
        tester = app.test_client()
        response = tester.get(
            '/applications',
            content_type='html/text'
        )
        self.assertTrue(b'<h1>404 Seems you got lost</h1>' in response.data)

    # Ensure that the error page loads correctly
    def test_changepassword(self):
        tester = app.test_client()
        response = tester.get(
            '/change_password/abcdefg',
            content_type='html/text'
        )
        self.assertTrue(b'<h1>404 Seems you got lost</h1>' in response.data)

    # Ensure that the error page loads correctly
    def test_editapplication(self):
        tester = app.test_client()
        response = tester.get(
            '/edit_application',
            content_type='html/text'
        )
        self.assertTrue(b'<h1>404 Seems you got lost</h1>' in response.data)

    # Ensure that the error page loads correctly
    def test_editapplicationId(self):
        tester = app.test_client()
        response = tester.get(
            '/edit_application/abcdef',
            content_type='html/text'
        )
        self.assertTrue(b'<h1>404 Seems you got lost</h1>' in response.data)

    # Ensure that the error page loads correctly
    def test_edituser(self):
        tester = app.test_client()
        response = tester.get(
            '/edit_user',
            content_type='html/text'
        )
        self.assertTrue(b'<h1>404 Seems you got lost</h1>' in response.data)

    # Ensure that the error page loads correctly
    def test_edituserId(self):
        tester = app.test_client()
        response = tester.get(
            '/edit_user/abcdef',
            content_type='html/text'
        )
        self.assertTrue(b'<h1>404 Seems you got lost</h1>' in response.data)

    # Ensure that the error page loads correctly
    def test_editvacancy(self):
        tester = app.test_client()
        response = tester.get(
            '/edit_vacancy',
            content_type='html/text'
        )
        self.assertTrue(b'<h1>404 Seems you got lost</h1>' in response.data)

    # Ensure that the error page loads correctly
    def test_editvacancyId(self):
        tester = app.test_client()
        response = tester.get(
            '/edit_vacancy/abcdef',
            content_type='html/text'
        )
        self.assertTrue(b'<h1>404 Seems you got lost</h1>' in response.data)

    # Ensure that the error page loads correctly
    def test_profile(self):
        tester = app.test_client()
        response = tester.get(
            '/profile',
            content_type='html/text'
        )
        self.assertTrue(b'<h1>404 Seems you got lost</h1>' in response.data)

    # Ensure that the error page loads correctly
    def test_users(self):
        tester = app.test_client()
        response = tester.get(
            '/users',
            content_type='html/text'
        )
        self.assertTrue(b'<h1>404 Seems you got lost</h1>' in response.data)


class loginTests(unittest.TestCase):
    '''
    testClass for all login functionality
    '''
    # Test for login by user with correct credentials
    def test_correct_credentials_user(self):
        tester = app.test_client()
        response = tester.post(
            '/login',
            data=dict(username=USERNAME_USER, password=SPW_TWO),
            follow_redirects=True
        )
        self.assertIn(b'<h1>Welcome to BOS UP</h1>', response.data)

    # Test for login by user with incorrect username
    def test_incorrect_username_user(self):
        tester = app.test_client()
        response = tester.post(
            '/login',
            data=dict(username='randomusername', password=SPW_TWO),
            follow_redirects=True
        )
        self.assertIn(b'The username provided is not known', response.data)

    # Test for login by user with incorrect password
    def test_incorrect_password_user(self):
        tester = app.test_client()
        response = tester.post(
            '/login',
            data=dict(username=USERNAME_USER, password='randompassword'),
            follow_redirects=True
        )
        self.assertIn(b'Your password is incorrect', response.data)

    # Test for login by admin with correct credentials
    def test_correct_credentials_admin(self):
        tester = app.test_client()
        response = tester.post(
            '/login',
            data=dict(username=USERNAME_ADMIN, password=SPW_ONE),
            follow_redirects=True
        )
        self.assertIn(b'<h1>Welcome to BOS UP</h1>', response.data)

    # Test for login by admin with incorrect username
    def test_incorrect_username_admin(self):
        tester = app.test_client()
        response = tester.post(
            '/login',
            data=dict(username='randomusername', password=SPW_ONE),
            follow_redirects=True
        )
        self.assertIn(b'The username provided is not known', response.data)

    # Test for login by admin with incorrect password
    def test_incorrect_password_admin(self):
        tester = app.test_client()
        response = tester.post(
            '/login',
            data=dict(username=USERNAME_ADMIN, password='randompassword'),
            follow_redirects=True
        )
        self.assertIn(b'Your password is incorrect', response.data)


class RoutesUserAvailable(unittest.TestCase):
    '''
    testClass for all routes for a user of the site
    which are available for a user
    '''
    # Ensure that route opens index page
    def test_index(self):
        tester = app.test_client()
        tester.post(
            '/login',
            data=dict(username=USERNAME_USER, password=SPW_TWO),
            follow_redirects=True
        )
        response = tester.get(
            '/index',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 200)

    # Ensure that route opens vacancies page
    def test_vacancies(self):
        tester = app.test_client()
        tester.post(
            '/login',
            data=dict(username=USERNAME_USER, password=SPW_TWO),
            follow_redirects=True
        )
        response = tester.get(
            '/vacancies',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 200)

    # Ensure that route opens add application page
    def test_addapplicationFromVacancy(self):
        tester = app.test_client()
        tester.post(
            '/login',
            data=dict(username=USERNAME_USER, password=SPW_TWO),
            follow_redirects=True
        )
        response = tester.get(
            f'/add_application/{VACANCY_ID}',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 200)

    # Ensure that route opens my applications page
    def test_applications(self):
        tester = app.test_client()
        tester.post(
            '/login',
            data=dict(username=USERNAME_USER, password=SPW_TWO),
            follow_redirects=True
        )
        response = tester.get(
            '/myapplications',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 200)

    # Ensure that route opens profile page
    def test_profile(self):
        tester = app.test_client()
        tester.post(
            '/login',
            data=dict(username=USERNAME_USER, password=SPW_TWO),
            follow_redirects=True
        )
        response = tester.get(
            f'/profile/{CANDIDATE_ID_USER}',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 200)


# To run the test app
if __name__ == "__main__":
    unittest.main()
