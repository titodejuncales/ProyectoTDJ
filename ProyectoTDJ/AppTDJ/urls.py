from django.urls import path
from AppTDJ.views import *

urlpatterns = [
    path('', inicio, name ="Inicio"),
    path('camisetasnacionales/', camNacionales, name ="Camnac"),
    path('camisetasinternacionales/', camInternacionales, name = "Camint"),
    path('camisetasselecciones/', camSelecciones, name = "Camsel"),
    path('camnacform/', camNacForm, name="CamNacForm"),
    path('camintform/', camIntForm, name="CamIntForm"),
    path('camselform/', camSelForm, name="CamSelForm"),
    path('resultcamint/', resultCamInt, name="CamIntRes"),
    path('resultcamnac/', resultCamNac, name="CamNacRes"),
    path('resultcamsel/', resultCamSel, name="CamSelRes"),
    path('camintbuscar/', busquedaCamInt, name="CamIntBusc"),
    path('camnacbuscar/', busquedaCamNac, name="CamNacBusc"),
    path('camselbuscar/', busquedaCamSel, name="CamSelBusc"),
]