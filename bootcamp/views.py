from django.shortcuts import render

# Create your views here.

#Importar HTTPRsponse
from django.http import HttpResponse
#Cliente pide Request
#Servidor Responde Respose
def get_koder(request):
    #Response
    return HttpResponse("Este es el koder")

def list_koder(request):
    return HttpResponse("Esta es la lista de koders: ")

