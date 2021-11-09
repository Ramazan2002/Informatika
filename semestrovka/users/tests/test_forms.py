from django.test import TestCase
from users.forms import RegistrationForm, AuthorizationForm, EditProfile, EditGroup

class RegistrationFormTest(TestCase):

    def test_labels(self):
        form = RegistrationForm()
        self.assertTrue(form.fields['login'].label == 'login')
        self.assertTrue(form.fields['password'].label == 'password')
        self.assertTrue(form.fields['password_repeat'].label == 'password repeat')

    def test_check_valid(self):
        data = {'login': '123456', 'password': '123456789', 'password_repeat': '123456789'}
        form = RegistrationForm(data=data)
        self.assertTrue(form.is_valid())

class AuthorizationFormTest(TestCase):

    def test_labels(self):
        form = AuthorizationForm()
        self.assertTrue(form.fields['login'].label == 'login')
        self.assertTrue(form.fields['password'].label == 'password')

    def test_check_valid(self):
        data = {'login': '123456', 'password': '123456789'}
        form = AuthorizationForm(data=data)
        self.assertTrue(form.is_valid())

class EditProfileFormTest(TestCase):

    def test_labels(self):
        form = EditProfile()
        self.assertTrue(form.fields['name'].label == 'Name')
        self.assertTrue(form.fields['email'].label == 'Email')
        self.assertTrue(form.fields['password'].label == 'Change password')

    def test_check_valid(self):
        data = {'name': 'testname', 'email': 'testemail@email.com', 'password': '123456789'}
        form = EditProfile(data=data)
        print(form.errors)
        self.assertTrue(form.is_valid())
