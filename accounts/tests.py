from django import forms
from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.http import HttpRequest
from django.test import TestCase, RequestFactory, Client
from rest_framework.request import Request
from .backends import EmailAuth
from .forms import UserRegistrationForm
from .models import User


# checking that users can login to their accounts
class SimpleTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.client = Client()
        self.user = User.objects.create_user(username='None', email='test@test.com', password='letmein1')
        self.client.format_kwarg = ''

        self.factory = RequestFactory()
        RequestFactory(username='None', email='test@test.com', password='letmein1')

        self.request = Request(HttpRequest())
        self.request.__setattr__('user', self.request.user)
        self.client.request = self.request

    def test_details(self):
        # Create an instance of a GET request.
        request = self.factory.get('/templates/profile')

        # Recall that middleware are not supported. You can simulate a
        # logged-in user by setting request.user manually.
        request.user = self.user


# checking various scenarios that occur when users submit valid, invalid or missing data
class TestRegistration(TestCase):

    def test_manager_create(self):
        user = User.objects._create_user(None, "test@test.com", "password", False, False)
        self.assertIsNotNone(user)

        with self.assertRaises(ValueError):
            user = User.objects._create_user(None, None, "password", False, False)

    def test_registration_form(self):
        form = UserRegistrationForm({
            'email': 'test@test.com',
            'password1': 'letmein1',
            'password2': 'letmein1',
            'stripe_id': settings.STRIPE_SECRET,
            'credit_card_number': 4242424242424242,
            'cvv': 123,
            'expiry_month': 1,
            'expiry_year': 2033
        })

        self.assertTrue(form.is_valid())

    def test_registration_form_fails_with_missing_email(self):
        form = UserRegistrationForm({
            'password1': 'letmein1',
            'password2': 'letmein1',
            'stripe_id': settings.STRIPE_SECRET,
            'credit_card_number': 4242424242424242,
            'cvv': 123,
            'expiry_month': 1,
            'expiry_year': 2033
        })

        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError, "Please enter your email address", form.full_clean())

    def test_registration_fails_with_empty_password1(self):
        form = UserRegistrationForm({
            'email': 'test@test.com',
            'password2': 'letmein1',
            'stripe_id': settings.STRIPE_SECRET,
            'credit_card_number': 4242424242424242,
            'cvv': 123,
            'expiry_month': 1,
            'expiry_year': 2033
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError, "Passwords do not match", form.full_clean())

    def test_registration_fails_with_empty_password2(self):
        form = UserRegistrationForm({
            'email': 'test@test.com',
            'password1': 'letmein1',
            'stripe_id': settings.STRIPE_SECRET,
            'credit_card_number': 4242424242424242,
            'cvv': 123,
            'expiry_month': 1,
            'expiry_year': 2033
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError, "Passwords do not match", form.full_clean())

    def test_registration_form_fails_wih_passwords_that_dont_match(self):
        form = UserRegistrationForm({
            'email': 'test@test.com',
            'password1': 'letmein1',
            'password2': 'letmein3',
            'stripe_id': settings.STRIPE_SECRET,
            'credit_card_number': 4242424242424242,
            'cvv': 123,
            'expiry_month': 1,
            'expiry_year': 2033
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError, "Passwords do not match", form.full_clean())

    def test_registration_fails_with_empty_credit_card(self):
        form = UserRegistrationForm({
            'email': 'test@test.com',
            'password1': 'letmein1',
            'stripe_id': settings.STRIPE_SECRET,
            'credit_card_number': 4242424242424242,
            'cvv': 123,
            'expiry_month': 1,
            'expiry_year': 2033
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError, "Credit card number not entered.Please enter a valid card number in format xxxxxxxxxxxxxx1234.", form.full_clean())

    def test_registration_form_fails_with_credit_cards_that_dont_match(self):
        form = UserRegistrationForm({
            'email': 'test@test.com',
            'password1': 'letmein1',
            'password2': 'letmein3',
            'stripe_id': settings.STRIPE_SECRET,
            'credit_card_number': 4242424242424242,
            'cvv': 123,
            'expiry_month': 1,
            'expiry_year': 2033
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError, "Invalid credit card no.Please enter again", form.full_clean())

    def test_registration_fails_with_empty_cvv(self):
        form = UserRegistrationForm({
            'email': 'test@test.com',
            'password1': 'letmein1',
            'stripe_id': settings.STRIPE_SECRET,
            'credit_card_number': 4242424242424242,
            'cvv': 123,
            'expiry_month': 1,
            'expiry_year': 2033
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError, "CVV not entered.Please enter a CVV.", form.full_clean())

    def test_registration_form_fails_with_cvv_that_dont_match(self):
        form = UserRegistrationForm({
            'email': 'test@test.com',
            'password1': 'letmein1',
            'password2': 'letmein3',
            'stripe_id': settings.STRIPE_SECRET,
            'credit_card_number': 4242424242424242,
            'cvv': 123,
            'expiry_month': 1,
            'expiry_year': 2033
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError, "Invalid CVV no.Please enter a CVV in format xxx.",form.full_clean())

    def test_home_page_status_code_is_ok(self):
        home_page = self.client.get('/')
        self.assertEquals(home_page.status_code, 200)


# checking that the backend can validate user data
class TestBackends(TestCase):
    def test_authenticate_invalid(self):
        email_auth = EmailAuth()
        user = email_auth.authenticate()
        self.assertIsNone(user)

    def test_authenticate_valid(self):
        email = "test@test.com"
        password = "password"
        new_user = User.objects._create_user(None, email, password, False, False)
        email_auth = EmailAuth()
        user = email_auth.authenticate(email, password)
        self.assertEquals(new_user, user)

    def authenticate(self, username=None, password=None):
        login_valid = (settings.ADMIN_LOGIN == username)
        pwd_valid = check_password(password, settings.ADMIN_PASSWORD)
        if login_valid and pwd_valid:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                # Create a new user. Note that we can set password
                # to anything, because it won't be checked; the password
                # from settings.py will.
                user = User(username=username, password='get from settings.py')
                user.is_staff = True
                user.is_superuser = True
                user.save()
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

# checking that user data can be posted, and that they are redirected to their account profile or the logout page
class ExamplePostTest(TestCase):
    @classmethod
    def setUpTestData(self):
        self.client = Client()


    def test_addAccount(self):
        response = self.client.post('/',username='None', email='none@none.com', password='letmein1')
        self.assertEqual(response.status_code, 200)


def test_profile(self):
        # Issue a GET request.
        response = self.client.get('/profile.html/')

        # Check that the response is 200 OK.
        self.assertEquals(response.status_code, 200)


def test_logout(self):
        # Issue a GET request.
        response = self.client.get('/index.html/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(b'{"messages": "You have successfully logged out"}', response.content)