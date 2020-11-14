from django import forms 
from .models import Core
from django.contrib.auth.models import User



class PostForm(forms.ModelForm):

    
    class Meta:
        
        model  = User
        fields = '__all__'

