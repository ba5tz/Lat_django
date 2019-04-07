from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'heading':'Selamat Datang',
        'subheading':'di web pertama dengan django',
        'judul':'andi',
        'nav':[
            ['/','Home' ],
            ['/blog','Blog'],
            ['/about','About'],
        ]
    }
    return render(request, 'index.html', context)
