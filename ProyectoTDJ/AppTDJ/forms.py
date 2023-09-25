from django import forms

class CamNacForm(forms.Form):
    nombre = forms.CharField()
    club = forms.CharField()
    marca = forms.CharField()
    year = forms.IntegerField()
    talle = forms.CharField()
    colores = forms.CharField()

class CamIntForm(forms.Form):
    nombre = forms.CharField()
    club = forms.CharField()
    marca = forms.CharField()
    year = forms.IntegerField()
    talle = forms.CharField()
    colores = forms.CharField()

class CamSelForm(forms.Form):
    nombre = forms.CharField()
    pais = forms.CharField()
    marca = forms.CharField()
    year = forms.IntegerField()
    talle = forms.CharField()
    colores = forms.CharField()
