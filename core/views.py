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

    variables= {
         'genero':genero,
          'region':region,
          'ciudad':ciudad,
          'vivienda':vivienda,
          'usuario':usuario
    }

    if request.POST:
        usuario= Usuario()
        usuario.rut_usuario=request.POST.get('txtRun')
        usuario.nombre=request.POST.get('txtNombre')
        usuario.ap_pat=request.POST.get('txtApPat')
        usuario.ap_mat=request.POST.get('txtApMat')

        genero=Genero()
        genero.id=int(request.POST.get('cboGenero'))
        usuario.genero=genero



        usuario.fec_nac=request.POST.get('txtNacimiento')
        usuario.telefon=request.POST.get('txtfono')

        region=Region()
        region.id=int(request.POST.get('cboRegion'))
        usuario.region=region


        #error al registrar comuna 
        ciudad=Comuna()
        ciudad.id=int(request.POST.get('cboCuidad'))
        usuario.ciudad=ciudad


        usuario.direccion=request.POST.get('txtDireccion')
        usuario.mail=request.POST.get('txtMail')


        tipoVivienda=Tipo_Vivienda()
        tipoVivienda.id=int(request.POST.get('cboTipoVivienda'))
        usuario.tipoVivienda=tipoVivienda



        tipoUsuario=Tipo_usuario()
        tipoUsuario.id=int(request.POST.get('cboUser'))
        usuario.tipoUsuario=tipoUsuario


        try:
            usuario.save()
            variables['mensaje']= "Se registro el usuario"
        except Exception as a:
            variables['mensaje']= "Error al registrar Usuario" + str(a)
            




    return render(request, 'core/registro.html',variables)

def registroComunas(request,id):  #nuevo metodo view que filtra las comunas segun el id rescatado
    ciudad=Comuna.objects.filter(idregion=id) #filtro por idregion (id de clase en models.py)
    return render(request, 'core/comboComuna.html',{ #usa el html combo comuna para escribir los opcion
          'ciudad':ciudad, #retorna tambien la ciudad
   })









