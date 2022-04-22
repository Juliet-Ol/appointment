from django import forms
from .models import Profile, Appointment
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User  

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


class SignupForm(UserCreationForm):  
    email = forms.EmailField(max_length=200, help_text='Required')  
    class Meta:  
        model = User  
        fields = ('username', 'email', 'password1', 'password2')  