from django.test import TestCase, Client
from django.urls import reverse
from .models import CustomeUser
from .forms import CustomeUserRegistrationFrom, CustomeUserLoginForm
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model 
from django.contrib.auth import get_user_model

class TestCaseCustomeUser(TestCase):
    def setUp(self):
        self.user = CustomeUser.objects.create_user(
            username = 'testuser',
            email = 'testuser@gmail.com',
            password = '1234'
        )

        self.admin_user = CustomeUser.objects.create_superuser(
            username='adminuser',
            email='adminuser@gmail.com',
            password='admin1234'
        )
    
    def test_create_user(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'testuser@gmail.com')
        self.assertTrue(self.user.check_password('1234'))

    def test_create_superuser(self):
        self.assertEqual(self.admin_user.username, 'adminuser')
        self.assertEqual(self.admin_user.email, 'adminuser@gmail.com')
        self.assertTrue(self.admin_user.check_password('admin1234'))
        self.assertTrue(self.admin_user.is_superuser)
        self.assertTrue(self.admin_user.is_staff)
    
    def test_not_superuser(self):
        self.assertFalse(self.user.is_superuser)
        self.assertFalse(self.user.is_staff)

    def test_modify_username(self):
        new_username = "newusername"
        self.user.username = new_username
        self.user.save()
        self.assertEqual(self.user.username, new_username)

    def test_delete_user(self):
        user_id = self.user.id
        self.user.delete()
        with self.assertRaises(CustomeUser.DoesNotExist):
            CustomeUser.objects.get(id=user_id)
    
    def test_email_validation(self):
        invalid_email = 'invalidemail'
        with self.assertRaises(ValidationError):
            user = CustomeUser.objects.create_user(username='test', email=invalid_email, password='password')
            user.full_clean()

    def test_login_user(self):
        logged_in_user = CustomeUser.objects.get(username=self.user.username)
        self.assertEqual(self.user.id, logged_in_user.id)


class TestCaseCustomeUserRegistrationForm(TestCase):
    def test_required_fields(self):
        form = CustomeUserRegistrationFrom(data={})
        self.assertFalse(form.is_valid())
        self.assertTrue(form.has_error('username', 'required'))
        self.assertTrue(form.has_error('email', 'required'))
        self.assertTrue(form.has_error('password1', 'required'))
        self.assertTrue(form.has_error('password2', 'required'))
    
    def test_registration_form(self):
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword',
        }
        form = CustomeUserRegistrationFrom(data=form_data)
        self.assertTrue(form.is_valid())

    def test_registration_form_password_mismatch(self):
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpassword',
            'password2': 'differentpassword',
        }
        form = CustomeUserRegistrationFrom(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)

class TestCaseCustomeUserLoginForm(TestCase):
    def setUp(self):
        self.user = CustomeUser.objects.create_user(
            username='testuser', 
            email='test@example.com', 
            password='testpassword'
        )

    def test_login_form(self):
        form_data = {
            'username': 'testuser',
            'password': 'testpassword',
        }
        form = CustomeUserLoginForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_login_form_missing_password(self):
        form_data = {
            'username': 'testuser',
        }
        form = CustomeUserLoginForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password', form.errors)


class TestCaseSignUpView(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')

    def test_signup(self):
        response = self.client.post(self.register_url, {
            'username': 'testusersignup',
            'email': 'testusersignup@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword',
        })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(CustomeUser.objects.filter(username="testusersignup").exists())
        self.assertTrue(CustomeUser.objects.filter(email="testusersignup@example.com").exists())


class TestCaseSignInView(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.profile_url = reverse('profile')
        self.user = get_user_model().objects.create_user(
            username='testusersignin',
            email='testusersignin@example.com',
            password='testpassword'
        )
    
    def test_signin(self):
        response = self.client.post(self.login_url, {
            'username': 'testusersignin',
            'password': 'testpassword'
        })

        self.assertEqual(response.status_code, 302) 
        self.assertRedirects(response, reverse('home')) 

    def test_redirect_for_unauthenticated_user(self):
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 302) 
        self.assertRedirects(response, f'{self.login_url}?next={self.profile_url}') 


class TestCaseProfilView(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.profile_url = reverse('profile')
        self.user = get_user_model().objects.create_user(
            username='testuserprofil',
            email='testuserprofil@example.com',
            password='testpassword'
        )

    def test_user_can_access_profile(self):
        self.client.login(username='testuserprofil', password='testpassword')
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)


 
    


