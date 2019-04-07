#views blog

from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    #print(posts)
    context = {
        'judul':'blog',
        'heading':'Blog',
        'subheading':'our new post',
        'Posts': posts,
    }
    return render(request,'blog/index.html',context)
