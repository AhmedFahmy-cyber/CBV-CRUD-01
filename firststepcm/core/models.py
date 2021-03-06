from django.db import models

from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User 
from ckeditor.fields import RichTextField




# Create your models here.
class Core(models.Model):

    title = models.CharField(max_length=200)
    excpert =RichTextField(null=True , blank=True)
    # excpert = models.TextField(null=True) 
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200 , unique=True)
    image = models.ImageField(upload_to ='uploads/')
    updated = models.DateTimeField(auto_now=True)
    puplished = models.DateTimeField(default=timezone.now)



    def get_absolute_url(self):
        return reverse("core:singleview", args=[self.slug] )
        
    def posts_absolute_url(self):
        return reverse("core:posts" )

    def form_absolute_url(self):
        return reverse("core:posts" )   

    def edit_absolute_url(self):
        return reverse("core:EditView" , args=[self.pk])  

    def edit_absolute_url(self):
        return reverse("core:EditView" , args=[self.pk]) 


    def delete_absolute_url(self):
        return reverse("core:delete" , args=[self.pk])       
    
    class Meta:

        ordering = ['-puplished']
        verbose_name_plural = 'Core'


    def __str__(self):

        return self.title     