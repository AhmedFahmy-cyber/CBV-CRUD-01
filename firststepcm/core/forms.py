from django import form 
from .mpdels import Core



class PostForm(forms.ModelForm):

    
    class Meta:
        
        model = Core
        fields = '__all__'
