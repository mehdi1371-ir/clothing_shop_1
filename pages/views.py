from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, FormView

from .models import AboutUs, OurTeam, OurService
from .forms import ContactUsForm


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(ListView):
    model = AboutUs
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutPageView, self).get_context_data(**kwargs)
        context['abouts'] = AboutUs.objects.all()
        context["teams"] = OurTeam.objects.all()
        context['services'] = OurService.objects.all()
        return context


class ContactUsFormView(FormView):
    template_name = 'pages/contact_us.html'
    form_class = ContactUsForm
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)