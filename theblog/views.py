from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Post
from .forms import PostForm

# def profile(request):
#     return render(request, 'profile.html')

# def directory(request):
#     return render(request, 'directory.html')

class ProfileView(TemplateView):
    model = Post
    template_name = 'profile.html'

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    # ordering =['-id'] #shows notices in reverse order
    ordering =['-post_date'] 
    

class ArticleDetailView(DetailView):
    model= Post
    template_name = 'article_details.html'

class AddPostView(CreateView):
    model= Post
    form_class= PostForm
    template_name = 'add_post.html'
    # fields = '__all__'
    
class UpdatePostView(UpdateView):
    model=Post
    form_class= PostForm
    template_name = 'update_post.html'
    # fields = ['title','body']

class PostDeleteView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('home')