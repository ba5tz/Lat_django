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

def angka(request,input):
    heading = "<h1>Home</h1>"
    strangka = "angka :" + input
    str = heading + strangka
    return HttpResponse(str)

def tanggal(request,tahun):
    heading = "<h1>Page tanggal</h1>"
    strangka = "tahun :" + tahun
    str = heading + strangka
    return HttpResponse(str)
