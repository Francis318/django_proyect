from django.shortcuts import render
from django.template import loader

# Create your views here.

#Importar HTTPRsponse
from django.http import HttpResponse
#Cliente pide Request
#Servidor Responde Respose

from psicomedic.models import Psicologo, Paciente, Citas
def list_psicologits(request):
    psicologo_lis=Psicologo.objects.all()
    context={
        "psicologo":psicologo_lis
    }
    template=loader.get_template("templates/list_psicologo.html")
    return HttpResponse(template.render(context, request))


def get_psicologist(request,ids):
    #Response
    koders=Koder.objects.get(pk=ids)
    return HttpResponse(koders)

def list_patients(request):
    koders=Koder.objects.all()
    return HttpResponse(koders)

def get_patients(request,ids):
    #Response
    koders=Koder.objects.get(pk=ids)
    return HttpResponse(koders)

def list_appointments(request):
    koders=Koder.objects.all()
    return HttpResponse(koders)

def get_appointments(request,ids):
    #Response
    koders=Koder.objects.get(pk=ids)
    return HttpResponse(koders)



