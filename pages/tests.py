from urllib import response
from django.test import TestCase
from django.urls import reverse 


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
