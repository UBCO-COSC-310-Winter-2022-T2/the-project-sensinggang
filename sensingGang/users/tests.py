from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.

class LoginTestCases(TestCase):
    
    # User setup
    def setUp(self):
        self.client = Client()
        self.username = 'testuser'
        self.password = 'password'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        
    # Test for login 
    def test_valid_login(self):
        response = self.client.post(reverse('login'), {'username': self.username, 'password': self.password})
        # Check response status code is 200 (This means OK)
        self.assertEqual(response.status_code, 200)
        # Check if user is then logged in
        self.assertIn('_auth_user_id', self.client.session)
    
    # Test for invalid login and correct error message
    def test_invalid_login(self):
        response = self.client.post(reverse('login'), {'username': self.username, 'password': 'wrongPassword'})
        # Checking invalid message and OK status code
        self.assertContains(response, "Username or password incorrect", status_code=200)
        # Checking if not in logged in users (no valid session key)
        self.assertNotIn('_auth_user_id', self.client.session)
        
class AccountCreationTestCases(TestCase):
    
    # User setup
    def setUp(self):
        self.client = Client()
        self.username = 'testuser'
        self.password = 'password'
        self.create_account_url = reverse('create_account')
        
    def test_valid_account_creation(self):
        response = self.client.post(self.create_account_url, {'username': self.username , 'password1': self.password, 'password2': self.password})
        # Checks for valid redirect to main page
        self.assertRedirects(response, reverse('main'), status_code=302, target_status_code=200)
        # Verify that the user was created and can log in.
        self.assertEqual(User.objects.count(), 1)
        self.assertIsNotNone(User.objects.get(username=self.username).pk)
    
    def test_matching_passwords(self):
        response = self.client.post(self.create_account_url, {'username': self.username, 'password1': self.password, 'password2': 'difPassword'})
        # Check for correct message for unmatching passwords
        self.assertContains(response, "Passwords do not match", status_code=200)
        # Check if not user object was created
        self.assertEqual(User.objects.count(), 0)
        
    def test_empty_fields(self):
        response = self.client.post(self.create_account_url, {'username': '', 'password1': '', 'password2': ''})
        # Check for correct message for empty fields
        self.assertContains(response, "This field is required", status_code=200)
        # Check if not user object was created
        self.assertEqual(User.objects.count(), 0)