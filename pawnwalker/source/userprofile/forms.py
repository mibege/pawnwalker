from django import forms
from django.shortcuts import get_object_or_404

from accounts.models import Event
from userprofile.models import userProfile
from django.utils.translation import gettext_lazy as _
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput

from userprofile.widget import BootstrapDateTimePickerInput


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = userProfile
        fields = ['name', 'address', 'city', 'isDogwalker']

    def save(self, commit=True):
        auction = super(UserProfileForm, self).save(commit=False)
        if commit:
            auction.save()
        return auction


class AdvertForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(AdvertForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(AdvertForm, self).save(commit=False)
        instance.user = self.request.user

        if commit:
            instance.save()
        return instance


class DateForm(forms.Form):
    date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])

class DateForm(forms.Form):
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=BootstrapDateTimePickerInput()
    )


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'start_date', 'end_date']
        widgets = {
            'start_date': DatePickerInput(),  # default date-format %m/%d/%Y will be used
            'end_date': DatePickerInput(format='%Y-%m-%d'),  # specify date-frmat
        }