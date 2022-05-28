from django.views.generic import TemplateView, ListView

from .models import AboutUs, OurTeam, OurService


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

    