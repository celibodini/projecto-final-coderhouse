from django import forms
from ejemplo.models import Celulares

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100)


class CelularesForm(forms.ModelForm):
  class Meta:
    model = Celulares
    fields = ['nombre', 'marca', 'precio']