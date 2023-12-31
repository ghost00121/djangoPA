from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.erp.forms import PagoNivelForm
from core.erp.models import  PagoNivel

class PagosListView(ListView):
    model = PagoNivel
    template_name = 'pagos/list.html'

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
                for i in PagoNivel.objects.all():
                    data.append(i.toJSON())
            
            else:
                data['error'] = 'Ha ocurrido un error' # Si no es 'searchdata', asignar un diccionario de error
        except Exception as e:
            data = {'error': str(e)}  # Si hay una excepción, asignar un diccionario de error
        return JsonResponse(data, safe=False)  # Retorna los datos en formato JSON

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Pagos'
        context['create_url'] = reverse_lazy('erp:pagos_create')
        context['list_url'] = reverse_lazy('erp:pagos_list')
        context['entity'] = 'Pagos'
        return context

class PagosCreateView(CreateView):
    model = PagoNivel
    form_class = PagoNivelForm
    template_name = 'pagos/create.html'
    success_url = reverse_lazy('erp:pagos_list')

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
        context['title'] = 'Creación de un Pago'
        context['entity'] = 'Pagos'
        context['list_url'] = reverse_lazy('erp:pagos_list')
        context['action'] = 'add'
        return context

class PagosUpdateView(UpdateView):
    model = PagoNivel
    form_class = PagoNivelForm
    template_name = 'pagos/create.html'
    success_url = reverse_lazy('erp:pagos_list')

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
        context['title'] = 'Edición de un Pago '
        context['entity'] = 'Pagos'
        context['list_url'] = reverse_lazy('erp:pagos_list')
        context['action'] = 'edit'
        return context

class PagosDeleteView(DeleteView):
    model = PagoNivel
    template_name = 'pagos/delete.html'
    success_url = reverse_lazy('erp:pagos_list')

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
        context['title'] = 'Eliminación de un pago'
        context['entity'] = 'Pagos'
        context['list_url'] = reverse_lazy('erp:pagos_list')
        return context
