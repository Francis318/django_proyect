from django.shortcuts import render
from django.template import loader

# Create your views here.

#Importar HTTPRsponse
from django.http import HttpResponse
#Cliente pide Request
#Servidor Responde Respose

from bootcamp.models import Koder
def list_koder(request):
    koders=Koder.objects.all()
    return HttpResponse(koders)


def get_koder(request,ids):
    #Response
    koders=Koder.objects.get(pk=ids)
    return HttpResponse(koders)


def list_mentors(request):
    context={
        "mentors": [
            {
                "name": "Benjamin",
                "last_name": "Aguilar",
                "is_active": True
            },
            {
                "name": "Alfredo",
                "last_name": "Altamirano",
                "is_active": True
            },
            {
                "name": "Charles",
                "last_name": "Lopez",
                "is_active": False
            },
        ]
    }
    template=loader.get_template("templates/list_mentors.html")
    return HttpResponse(template.render(context,request))