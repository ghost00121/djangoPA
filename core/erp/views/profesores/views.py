from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.erp.forms import ProfesoresForm  # Cambia el nombre del formulario
from core.erp.models import Profesores  # Cambia el modelo

class ProfesoresListView(ListView):  # Cambia el nombre de la clase
    model = Profesores  # Cambia el modelo
    template_name = 'profesores/list.html'  # Cambia el nombre de la plantilla

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Profesores.objects.all():
                    data.append(i.toJSON())
            
            else:
                data['error'] = 'Ha ocurrido un error' # Si no es 'searchdata', asignar un diccionario de error
        except Exception as e:
            data = {'error': str(e)}  # Si hay una excepción, asignar un diccionario de error
        return JsonResponse(data, safe=False)  # Retorna los datos en formato JSON

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Profesores'  # Cambia el título
        context['create_url'] = reverse_lazy('erp:profesores_create')  # Cambia el nombre de la URL para crear docentes
        context['list_url'] = reverse_lazy('erp:profesores_list')  # Cambia el nombre de la URL para listar docentes
        context['entity'] = 'Profesores'  # Cambia la entidad
        return context

class ProfesoresCreateView(CreateView):  # Cambia el nombre de la clase
    model = Profesores  # Cambia el modelo
    form_class = ProfesoresForm  # Cambia el nombre del formulario
    template_name = 'profesores/create.html'  # Cambia el nombre de la plantilla
    success_url = reverse_lazy('erp:profesores_list')  # Cambia el nombre de la URL para listar docentes

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de un Docente'  # Cambia el título
        context['entity'] = 'Profesores'  # Cambia la entidad
        context['list_url'] = reverse_lazy('erp:profesores_list')  # Cambia el nombre de la URL para listar docentes
        context['action'] = 'add'
        return context

class ProfesoresUpdateView(UpdateView):  # Cambia el nombre de la clase
    model = Profesores  # Cambia el modelo
    form_class = ProfesoresForm  # Cambia el nombre del formulario
    template_name = 'profesores/create.html'  # Cambia el nombre de la plantilla
    success_url = reverse_lazy('erp:profesores_list')  # Cambia el nombre de la URL para listar docentes

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de un Profesor'  # Cambia el título
        context['entity'] = 'Profesores'  # Cambia la entidad
        context['list_url'] = reverse_lazy('erp:profesores_list')  # Cambia el nombre de la URL para listar docentes
        context['action'] = 'edit'
        return context

class ProfesoresDeleteView(DeleteView):  # Cambia el nombre de la clase
    model = Profesores  # Cambia el modelo
    template_name = 'profesores/delete.html'  # Cambia el nombre de la plantilla
    success_url = reverse_lazy('erp:profesores_list')  # Cambia el nombre de la URL para listar docentes

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de un profesor'  # Cambia el título
        context['entity'] = 'Profesores'  # Cambia la entidad
        context['list_url'] = reverse_lazy('erp:profesores_list')  # Cambia el nombre de la URL para listar docentes
        return context
