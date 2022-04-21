from django import forms
from .models import Profile, Appointment


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude =['user', 'identity_number']
        fields = '__all__'

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        exclude =['sent_date']
        fields = '__all__'        