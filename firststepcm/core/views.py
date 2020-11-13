from django.shortcuts import render
from django.views.generic import ListView , DetailView , UpdateView ,CreateView
from .models import *
from django.urls import reverse_lazy



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