from django.contrib import admin
from core.models import *
# Register your models here.


class MascotaAdmin(admin.ModelAdmin):
    list_display=('nombre','esterilizado')
    search_fields=['nombre']
    list_filter=('id_raza','cod_refugio')


class UsuarioAdmin(admin.ModelAdmin):
    list_display=('rut_usuario','nombre','ap_pat')
    search_fields=['rut_usuario']
    list_filter=('id_comuna','id_genero')





admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Tipo_Vivienda)
admin.site.register(Tipo_usuario)
admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Trabajador)
admin.site.register(Login)
admin.site.register(Fondo_Economico)
admin.site.register(Tipo_insumo)
admin.site.register(Transferencia)
admin.site.register(Insumo)
admin.site.register(Refugio)
admin.site.register(Raza)
admin.site.register(Origen_mascota)
admin.site.register(Mascota,MascotaAdmin)
admin.site.register(Visita_Medica)
admin.site.register(Tipo_campania)
admin.site.register(Campania)
admin.site.register(Campania_insumo)
admin.site.register(Visita_adopcion)
