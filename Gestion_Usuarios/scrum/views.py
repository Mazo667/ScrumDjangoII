from django.shortcuts import render
from django.http import HttpResponse

def pagina_principal(request):
    return HttpResponse("PAGINA PRINCIPAL")
