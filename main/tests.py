from django.test import TestCase, override_settings
from django.urls import reverse
from django.core import mail
from django.http import HttpResponse
from .forms import ContactForm 

# Create your tests here.

# Override email backend for tests
@override_settings(
    EMAIL_BACKEND='anymail.backends.mailgun.EmailBackend'
)

# Portfolio view/url tests
class PortfolioViewTests(TestCase):

    # About Url test
    def test_main_about_url_exists(self):
        response = self.client.get(reverse('main:about'))
        self.assertEqual(response.status_code, 200)

    # Contact Url test
    def test_main_contact_url_exists(self):
        response = self.client.get(reverse('main:contact'))
        self.assertEqual(response.status_code, 200)

    # Projects Url test
    def test_main_projects_url_exists(self):
        response = self.client.get(reverse('main:projects'))
        self.assertEqual(response.status_code, 200)

class PortfolioTemplateTests(TestCase):
    # About template test
    def test_about_template_used(self):
        response = self.client.get(reverse('main:about'))
        self.assertTemplateUsed(response, 'main/about.html')

    # Contact template test
    def test_contact_template_used(self):
        response = self.client.get(reverse('main:contact'))
        self.assertTemplateUsed(response, 'main/contact.html')

    # Projects template test
    def test_projects_template_used(self):
        response = self.client.get(reverse('main:projects'))
        self.assertTemplateUsed(response, 'main/projects.html')

    def test_contact_contains_downloadable_resume(self):
        response = self.client.get(reverse('main:contact'))
        self.assertContains(response, 'Download My Resume')

class ContactFormSubmissionTests(TestCase):
    # Valid form submission test
    def test_contact_form_valid_submission_sends_email(self):
        data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'message': 'Hello, this is a test message.',
        }
        response = self.client.post(reverse('main:contact'), data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn('Test User', mail.outbox[0].subject)

    # Invalid form submission test
    def test_contact_form_invalid_submission_returns_error(self):
        data = { # Missing input fields
            'name': '',
            'email': '',
            'message': '',
        }
        response = self.client.post(reverse('main:contact'), data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'name', 'This field is required.')
        self.assertFormError(response, 'form', 'email', 'This field is required.')
        self.assertFormError(response, 'form', 'message', 'This field is required.')


# Portfolio form tests
class ContactFormTests(TestCase):
    # Test valid form data
    def test_contact_form_valid(self):
        form_data = {
            'name': 'Ashley',
            'email': 'ashley@example.com',
            'message': 'Hello!'
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    # Test invalid form data
    def test_contact_form_invalid(self):
        form_data = {
            'name': '',
            'email': 'not-an-email',
            'message': ''
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)