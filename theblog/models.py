from distutils.command.upload import upload
import email
from email import header
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField

class Post(models.Model):
    title=models.CharField(max_length=255)
    header_image=models.ImageField(null=True,blank=True, upload_to="images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # body = models.TextField()
    body = RichTextField(blank=True,null=True)
    snippet = models.CharField(max_length=255)
    post_date=models.DateField(auto_now_add=True)
    # email= models.EmailField()
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        # return reverse("article-detail", kwargs={"pk": self.pk})
        return reverse('home')
    