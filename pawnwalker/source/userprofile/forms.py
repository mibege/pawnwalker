from django import forms

from userprofile.models import userProfile
from django.utils.translation import gettext_lazy as _


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = userProfile
        fields = ['address', 'city', 'isDogwalker']

    def save(self, commit=True):
        auction = super(UserProfileForm, self).save(commit=False)
        if commit:
            auction.save()
        return auction


class UpdateUserProfileForm(forms.Form):
    address = forms.CharField(label=_('Address'), max_length=30, required=False)
    city = forms.CharField(label=_('City'), max_length=150, required=False)
    isDogwalker = forms.BooleanField(label=_('Dog Walker'), required=False)
