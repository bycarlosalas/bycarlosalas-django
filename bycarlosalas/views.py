from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, context


def home(request):
    return render(request, 'index.html')

    # docextern=open("/Volumes/Macintosh Data/Users/usuario/Desktop/bycarlosalas.com/templates/sencillo.html")
    # templatehome=Template(docextern.read())
    # docextern.close()

    # contexthome=context()

    # renderhome=templatehome.render(contexthome)

    # return HttpResponse(renderhome)