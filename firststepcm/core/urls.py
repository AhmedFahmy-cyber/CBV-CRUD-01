from django.urls import path 
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .views import  IndexView ,SinglelView , PostsView ,AddView ,EditView ,Delete

app_name = "core"

urlpatterns = [
   
    path ('', login_required(IndexView.as_view()) , name = 'index'),
    path ('add/', AddView.as_view() , name = 'addview'),
    path ('posts/', staff_member_required(PostsView.as_view()) , name = 'posts'),
    path ('<slug:slug>/', SinglelView.as_view() , name = 'singleview'),
    path ('edit/<int:pk>/', EditView.as_view() , name = 'EditView'),
    path ('delete/<int:pk>/', Delete.as_view() , name = 'delete'),
]