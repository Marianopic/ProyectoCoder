from django.http import HttpResponse
from django.shortcuts import render

from django.template import loader

# Create your views here.
from AppCoder.models import Familiar

def crear_familiar(request):
    template = loader.get_template("template1.html")
    
    
    familiar_1 = Familiar(nombre ="Francisco", parentezco="Padre", edad="55", fecha_nacimiento ="30/03/1967")
    familiar_2 = Familiar(nombre ="Mariela", parentezco="Madre", edad="50", fecha_nacimiento ="30/03/1962")
    familiar_3 = Familiar(nombre ="Marina", parentezco="Hermana", edad="22", fecha_nacimiento ="30/03/2000")
    
    dict_de_contexto = {
    "familiar_1": familiar_1.nombre,
    "familiar_2": familiar_2.nombre,
    "familiar_3": familiar_3.nombre,
}

    res = template.render(dict_de_contexto)

    return HttpResponse(res)