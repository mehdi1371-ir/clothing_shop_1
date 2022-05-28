from django.test import TestCase
from django.urls import reverse 
from django.core import mail


class HomePageTest(TestCase):

    def test_home_page_url(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_home_page_url_with_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

class AboutPageTest(TestCase):
    
    def test_about_page_url(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_url_by_name(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

class ContactPageTest(TestCase):

    def test_contact_us_page_url(self):
        response = self.client.get('/contact_us/')
        self.assertEqual(response.status_code, 200)    

    def test_contact_us_page_url_by_name(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

    def test_contact_us_page_send_email(self):
        mail.send_mail('subject here', 'Here is the message.',
                'from@example.com', ['to@example.com'],)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'subject here')

