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
    print(context)
    template=loader.get_template("templates/list_psicologo.html")
    return HttpResponse(template.render(context, request))


def get_psicologist(request,ids):
    #Response
    psicologo_get=Psicologo.objects.get(pk=ids)
    context={
        "psicologo":psicologo_get
    }
    print(context)
    template=loader.get_template("templates/get_psicologo.html")
    return HttpResponse(template.render(context, request))

def list_patients(request):
    paciente_list=Paciente.objects.all()
    context={
        "paciente":paciente_list
    }
    template=loader.get_template("templates/list_paciente.html")
    return HttpResponse(template.render(context, request))

def get_patients(request,ids):
    #Response
    paciente_get=Paciente.objects.get(pk=ids)
    context={
        "paciente":paciente_get
    }
    template=loader.get_template("templates/get_paciente.html")
    return HttpResponse(template.render(context, request))

def list_appointments(request):
    citas_list=Citas.objects.all()
    context={
        "cita":citas_list
    }
    template=loader.get_template("templates/list_citas.html")
    return HttpResponse(template.render(context, request))

def get_appointments(request,ids):
    #Response
    citas_get=Citas.objects.get(pk=ids)
    context={
        "cita":citas_get
    }
    template=loader.get_template("templates/get_citas.html")
    return HttpResponse(template.render(context, request))


