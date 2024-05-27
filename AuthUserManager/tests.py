from django.test import TestCase
from .models import CustomeUser
from django.core.exceptions import ValidationError

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
