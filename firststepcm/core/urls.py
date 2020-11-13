from django.urls import path 

from .views import  IndexView ,SinglelView , PostsView ,AddView

app_name = "core"

urlpatterns = [
   
    path ('', IndexView.as_view() , name = 'index'),
    path ('add/', AddView.as_view() , name = 'addview'),
    path ('posts/', PostsView.as_view() , name = 'posts'),
    path ('<slug:slug>/', SinglelView.as_view() , name = 'singleview'),
]