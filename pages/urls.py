from django.urls import path

from .views import HomePageView, AboutPageView, ContactUsFormView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact_us/', ContactUsFormView.as_view(), name='contact'),
]
