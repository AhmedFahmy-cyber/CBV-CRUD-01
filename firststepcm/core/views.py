from django.shortcuts import render , redirect
from django.views.generic import ListView , DetailView , UpdateView ,CreateView
from .models import *
from django.urls import reverse_lazy
from django.contrib import messages


# Create your views here.

class IndexView(ListView):
    model = Core
    template_name = 'core/core_list.html'


class SinglelView(DetailView):
    model = Core
    template_name = "core/single.html"
    context_object_name = 'post'
    
class PostsView(ListView):
    model = Core
    template_name = 'core/posts.html'
    context_object_name = 'post_list'

class AddView(CreateView):
    model = Core
    template_name = 'core/add.html'
    fields = '__all__'
    success_url = reverse_lazy('core:posts')

class EditView(UpdateView):
    model = Core
    template_name = 'core/edit.html'
    fields = '__all__'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('core:posts')



    