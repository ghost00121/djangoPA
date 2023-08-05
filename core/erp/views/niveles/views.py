from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.erp.forms import NivelesForm
from core.erp.models import Niveles

class NivelesListView(ListView):
    model = Niveles
    template_name = 'niveles/list.html'

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
                for i in Niveles.objects.all():
                    data.append(i.toJSON())
            
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Niveles'
        context['create_url'] = reverse_lazy('erp:niveles_create')
        context['list_url'] = reverse_lazy('erp:niveles_list')
        context['entity'] = 'Niveles'
        return context

class NivelesCreateView(CreateView):
    model = Niveles
    form_class = NivelesForm
    template_name = 'niveles/create.html'
    success_url = reverse_lazy('erp:niveles_list')

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
        context['title'] = 'Creación de un Nivel'
        context['entity'] = 'Niveles'
        context['list_url'] = reverse_lazy('erp:niveles_list')
        context['action'] = 'add'
        return context

class NivelesUpdateView(UpdateView):
    model = Niveles
    form_class = NivelesForm
    template_name = 'niveles/create.html'
    success_url = reverse_lazy('erp:niveles_list')

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
        context['title'] = 'Edición de un Nivel'
        context['entity'] = 'Niveles'
        context['list_url'] = reverse_lazy('erp:niveles_list')
        context['action'] = 'edit'
        return context

class NivelesDeleteView(DeleteView):
    model = Niveles
    template_name = 'niveles/delete.html'
    success_url = reverse_lazy('erp:niveles_list')

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
        context['title'] = 'Eliminación de un Nivel'
        context['entity'] = 'Niveles'
        context['list_url'] = reverse_lazy('erp:niveles_list')
        return context
