from django.shortcuts import render
from django.template import loader

# Create your views here.

#Importar HTTPRsponse
from django.http import HttpResponse
#Cliente pide Request
#Servidor Responde Respose

def list_koder(request):
    context={
        "koders":[{"name": "Francisco", "generation":"1", "bootcamp": "Python","is_active":True,},
            {"name": "Martin", "generation":"1", "bootcamp": "Python","is_active":False,}]
    }
    template=loader.get_template("templates/list_koders.html")
    return HttpResponse(template.render(context,request))


def get_koder(request,id):
    #Response
    koders = [
        {"id": 0, "name": "Enrique", "generation": "1g", "bootcamp": "Python"},
        {"id": 1, "name": "Luis", "generation": "1g", "bootcamp": "Python"},
        {"id": 2, "name": "Irving", "generation": "1g", "bootcamp": "Python"},
    ]

    founded_koder = [koder for koder in koders if koder["id"] == id]
    return HttpResponse(f"Founder koder ---> {founded_koder}")

def list_mentors(request):
    context={
        "mentors":[{"name": "Alfredo", "generation":"1", "bootcamp": "Python","is_active":False,},
            {"name": "Ale", "generation":"1", "bootcamp": "Django","is_active":True,}]
    }
    template=loader.get_template("templates/list_mentors.html")
    return HttpResponse(template.render(context,request))