from django.shortcuts import render

# Create your views here.

#Importar HTTPRsponse
from django.http import HttpResponse
#Cliente pide Request
#Servidor Responde Respose
def bienvenida(request):
    #Response
    return HttpResponse("Bienvenidos Koders")

def despedida(request):
    return HttpResponse("Despedida")

def saludo(request):
    #Response
    return HttpResponse("Saludando a Koders")

def saludar_con_nombre(request, nombre):
    print("Imprimiendo: ",nombre)
    return HttpResponse(f"Hola {nombre}")

def Kodemia(request,type):
    if type=="mentor":
        print("Imprimiendo: ",type)
        return HttpResponse(f"Hola mentor, aqui estan tus clases")
    elif type=="koder":
            print("Imprimiendo: ",type)
            return HttpResponse(f"Hola koder, Bienvenido a Kodemia")
    else:
        return HttpResponse(f"No eres bienvenido")
