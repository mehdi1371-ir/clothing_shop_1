from django.contrib import admin

from .models import AboutUs, OurTeam, OurService


class OurTeamInline(admin.StackedInline):
    model = OurTeam
    extra = 0
    classes = ['collapse']


class OurServiceInline(admin.StackedInline):
    model = OurService
    extra = 0
    classes = ['collapse']


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    inlines = [OurTeamInline, OurServiceInline]
