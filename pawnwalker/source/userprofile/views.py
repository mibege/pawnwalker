from bootstrap_datepicker_plus import DateTimePickerInput
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from django.views.generic import FormView
from locationiq.geocoder import LocationIQ
from django.core import serializers

from accounts.models import Event
from userprofile.forms import UserProfileForm, DateForm, EventForm
from userprofile.models import userProfile


geocoder = LocationIQ('3aca79a02a3732')


class indexUserProfile(LoginRequiredMixin, FormView):
    template_name = 'accounts/profile/change_profile.html'
    model = userProfile
    form_class = UserProfileForm

    def form_valid(self, form):
        new_model = form.save(commit=False)
        new_model.user = self.request.user
        new_model.name = form.cleaned_data['name']
        new_model.address = form.cleaned_data['address']
        new_model.city = form.cleaned_data['city']
        new_model.isDogwalker = form.cleaned_data['isDogwalker']
        new_model.lat = convertToLat(form.cleaned_data['address'])
        new_model.lon = convertToLong(form.cleaned_data['address'])
        new_model.submitted_by = self.request.user
        new_model.save(self)
        messages.success(self.request, _('Profile data has been successfully updated.'))
        return redirect('index')


def indexMapProfile(request):
    template_name = 'accounts/profile/map.html'
    json_data = serializers.serialize("json", userProfile.objects.all(), cls=DjangoJSONEncoder)
    context = {'userProfile': userProfile.objects.all()}
    return render(request, template_name, context)


def indexDogWalkerBook(request, slug):
    template_name='accounts/profile/book.html'
    user = userProfile.objects.get(pk=slug)
    form_class = DateForm
    context = {'myvar': userProfile.objects.get(pk=slug),'userprofile':userProfile}
    return render(request,template_name,context)


def convertToLat(address):
    response = geocoder.geocode(str(address))
    lat = 0
    for r in response:
        lat = r['lat']

    return lat


def convertToLong(address):
    response = geocoder.geocode(str(address))
    lon = 0
    for r in response:
        lon = r['lon']

    return lon
