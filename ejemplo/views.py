from django.shortcuts import render, get_object_or_404
from ejemplo.models import Celulares
from ejemplo.forms import Buscar, CelularesForm 
from django.views import View


def monstrar_celulares(request):
  lista_celulares = Celulares.objects.all()
  return render(request, "ejemplo/celulares.html", {"lista_celulares": lista_celulares})

class BuscarCelular(View):
    form_class = Buscar
    template_name = 'ejemplo/buscar.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_celulares = Celulares.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_celulares': lista_celulares})
        return render(request, self.template_name, {"form": form})

class ActualizarCelular(View):
  form_class = CelularesForm
  template_name = 'ejemplo/actualizar_celular.html'
  initial = {"nombre":"", "marca":"", "precio":""}
  
  # prestar atención ahora el method get recibe un parametro pk == primaryKey == identificador único
  def get(self, request, pk): 
      familiar = get_object_or_404(Celulares, pk=pk)
      form = self.form_class(instance=Celulares)
      return render(request, self.template_name, {'form':form,'celular': Celulares})

  # prestar atención ahora el method post recibe un parametro pk == primaryKey == identificador único
  def post(self, request, pk): 
      familiar = get_object_or_404(Celulares, pk=pk)
      form = self.form_class(request.POST ,instance=Celulares)
      if form.is_valid():
          form.save()
          msg_exito = f"se actualizó con éxito el celular {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'celular': Celulares,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})

class AltaCelular(View):

    form_class = CelularesForm
    template_name = 'ejemplo/alta_celular.html'
    initial = {"nombre":"", "marca":"", "precio":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el celular {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})
