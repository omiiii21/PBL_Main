from django.urls import path
# from . import views
from .views import DirectoryView
urlpatterns = [
       path('directory/', DirectoryView.as_view(), name='directory')
]
