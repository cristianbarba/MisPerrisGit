from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def registro(request):
    genero=Genero.objects.all()
    region=Region.objects.all()
    ciudad=Comuna.objects.all()
    vivienda=Tipo_Vivienda.objects.all()
    usuario=Tipo_usuario.objects.all()
    return render(request, 'core/registro.html',{
          'genero':genero,
          'region':region,
          'ciudad':ciudad,
          'vivienda':vivienda,
          'usuario':usuario
    })

def registroComunas(request,id):  #nuevo metodo view que filtra las comunas segun el id rescatado
    ciudad=Comuna.objects.filter(idregion=id) #filtro por idregion (id de clase en models.py)
    return render(request, 'core/comboComuna.html',{ #usa el html combo comuna para escribir los opcion
          'ciudad':ciudad, #retorna tambien la ciudad
   })







