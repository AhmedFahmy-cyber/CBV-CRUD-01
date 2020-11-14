from django.contrib import messages
from django.shortcuts import render , redirect
from users.forms import RegisterForm 
from django.forms import ValidationError
# Create your views here.


def register(request):
    if request.method == 'POST':
        
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            # email = form.cleaned_data.get('email')
            # password1 = form.cleaned_data.get('password1')
            # password2 = form.cleaned_data.get('password2')
            # # form = RegisterForm(username=username,email=email,password=password,password2=password2)
            
            messages.success(request,f'Your account has been created you are now able to login')

            return redirect("users:login")
    else:
        form =   RegisterForm()  
    return render (request , 'users/register.html ', {'form':form})    