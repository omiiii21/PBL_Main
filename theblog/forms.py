from django import forms
from .models import Post    

class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields = ('title','author','header_image', 'body','snippet')
        
        widgets={
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control','value':'','id':'elder','type':'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            
            
        }