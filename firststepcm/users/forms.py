from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input label','placeholder': 'Enter your password'}),max_length=40, min_length=8)
    password2 = forms.CharField(max_length=40, min_length=8, label="Repeat password", widget=forms.PasswordInput(attrs={'class': 'input label','placeholder': 'Repeat password'}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input', 'autofocus': True ,'placeholder': 'Enter your username'}),
            'email': forms.EmailInput(attrs={'class': 'input', 'required': True ,'placeholder': 'Enter your email'}),
            # 'password':forms.PasswordInput(attrs={'class': 'input'}),
            # 'password2':forms.PasswordInput(attrs={'class': 'input'}),
        }

    

        