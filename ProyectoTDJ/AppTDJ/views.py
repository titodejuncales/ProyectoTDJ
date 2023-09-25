from django.shortcuts import render
from django.http import HttpResponse
from AppTDJ.models import *
from AppTDJ.forms import *

# Create your views here.

def inicio(request):
    return render(request, 'AppTDJ/inicio.html')

def camNacionales(request):
    return render(request, 'AppTDJ/camisetasnacionales.html')

def camInternacionales(request):
    return render(request, 'AppTDJ/camisetasinternacionales.html')

def camSelecciones(request):
    return render(request, 'AppTDJ/camisetasselecciones.html')

def camNacForm(request):
    if request.method == "POST":
        form1 = CamNacForm(request.POST)
        if form1.is_valid():
            info = form1.cleaned_data
            camnac = CamNacional(nombre=info["nombre"], club=info["club"], marca=info["marca"],
                             year=info["year"],talle=info["talle"],colores=info["colores"],
                               )
            camnac.save()
            return render(request, 'AppTDJ/camnaccreada.html')
    else:
        form1 = CamNacForm()
    return render(request, 'AppTDJ/camNacForm.html', {"form1":form1})

def camSelForm(request):
    if request.method == "POST":
        form1 = CamSelForm(request.POST)
        if form1.is_valid():
            info = form1.cleaned_data
            camnac = CamSeleccion(nombre=info["nombre"], pais=info["pais"], marca=info["marca"],
                             year=info["year"],talle=info["talle"],colores=info["colores"],
                               )
            camnac.save()
            return render(request, 'AppTDJ/inicio.html')
    else:
        form1 = CamSelForm()
    return render(request, 'AppTDJ/camSelForm.html', {"form1":form1})

def camIntForm(request):
    if request.method == "POST":
        form1 = CamIntForm(request.POST)
        if form1.is_valid():
            info = form1.cleaned_data
            camnac = CamInternacional(nombre=info["nombre"], club=info["club"], marca=info["marca"],
                             year=info["year"],talle=info["talle"],colores=info["colores"],
                               )
            camnac.save()
            return render(request, 'AppTDJ/inicio.html')
    else:
        form1 = CamIntForm()
    return render(request, 'AppTDJ/camIntForm.html', {"form1":form1})


def busquedaCamNac(request):
    return render(request, 'AppTDJ/busquedaCamNac.html')

def resultCamNac(request):
    if request.GET["club"]:
        camnac = request.GET["club"]
        camisetas = CamNacional.objects.filter(club__icontains=camnac)

        return render(request, "AppTDJ/resultcamNac.html", {"camisetas":camisetas, "camnac":camnac})

    else:
        return render(request, "AppTDJ/busquedaCamNac.html")


def busquedaCamInt(request):
    return render(request, 'AppTDJ/busquedaCamInt.html')

def resultCamInt(request):
    if request.GET["club"]:
        camint = request.GET["club"]
        camisetas = CamInternacional.objects.filter(club__icontains=camint)

        return render(request, "AppTDJ/resultcamInt.html", {"camisetas":camisetas, "camint":camint})

    else:
        return render(request, "AppTDJ/busquedaCamInt.html")


def busquedaCamSel(request):
    return render(request, 'AppTDJ/busquedaCamSel.html')

def resultCamSel(request):
    if request.GET["pais"]:
        camsel = request.GET["pais"]
        camisetas = CamSeleccion.objects.filter(pais__icontains=camsel)

        return render(request, "AppTDJ/resultcamSel.html", {"camisetas":camisetas, "camsel":camsel})

    else:
        return render(request, "AppTDJ/busquedaCamSel.html")
    
