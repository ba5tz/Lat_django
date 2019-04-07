from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'judul' : 'about',
        'heading':'About',
        'subheading':'Tentang kami',
    }
    return render(request,'about/index.html',context)
