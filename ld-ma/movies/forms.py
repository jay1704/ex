from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User,UserProfile
        
        
class SignUpForm(UserCreationForm):
        username = forms.CharField(max_length=30, required=False, help_text='Optional.')
        email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
        model = UserProfile
        class Meta:
                fields = ['username','password','password1','email']
        

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, required=False)
    email = forms.EmailInput()
    password = forms.CharField(widget=forms.PasswordInput)
    
