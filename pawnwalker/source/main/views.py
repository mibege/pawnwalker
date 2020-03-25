from django.shortcuts import render
from django.views.generic import TemplateView

from booking.models import Booking
from userprofile.models import userProfile


class IndexPageView(TemplateView):
    template_name = 'main/index.html'


class ChangeLanguageView(TemplateView):
    template_name = 'main/change_language.html'


def home(request):
    template_name = 'main/index.html'
    context = {'userProfile': userProfile , 'booking': Booking}
    return render(request, template_name, context)