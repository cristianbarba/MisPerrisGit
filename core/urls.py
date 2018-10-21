from django.urls import path
from .views import home,registro,registroComunas


urlpatterns = [
    path('', home, name="home"),
    path('registro/', registro, name="registro"), 
    path('combo/<id>/', registroComunas, name="combo"), #nueva url que ejecuta el filtro y captura la id //esta en el view
]

