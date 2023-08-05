from django.urls import path
from core.erp.views.dashboard.views import *
from core.erp.views.estudiantes.views import *
from core.erp.views.profesores.views import *
from core.erp.views.niveles.views import *
from core.erp.views.pagos.views import *




app_name = 'erp'

urlpatterns = [
    path('estudiantes/list/',EstudiantesListView.as_view(), name='estudiante_list'),
    path('estudiantes/add/', EstudiantesCreateView.as_view(), name='estudiante_create'),
    path('estudiantes/update/<int:pk>/', EstudiantesUpdateView.as_view(), name='estudiante_update'),
    path('estudiantes/delete/<int:pk>/', EstudiantesDeleteView.as_view(), name='estudiante_delete'),
     # Docentes
    path('profesores/list/', ProfesoresListView.as_view(), name='profesores_list'),
    path('profesores/add/', ProfesoresCreateView.as_view(), name='profesores_create'),
    path('profesores/update/<int:pk>/', ProfesoresUpdateView.as_view(), name='profesores_update'),
    path('profesores/delete/<int:pk>/', ProfesoresDeleteView.as_view(), name='profesores_delete'),
    
     # Niveles
    path('niveles/list/', NivelesListView.as_view(), name='niveles_list'),
    path('niveles/add/', NivelesCreateView.as_view(), name='niveles_create'),
    path('niveles/update/<int:pk>/', NivelesUpdateView.as_view(), name='niveles_update'),
    path('niveles/delete/<int:pk>/', NivelesDeleteView.as_view(), name='niveles_delete'),
    # home
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    # home
    path('pagoslist/', PagosListView.as_view(), name='pagos_list'),
    path('pagos/create/', PagosCreateView.as_view(), name='pagos_create'),
    path('pagos/update/<int:pk>/', PagosUpdateView.as_view(), name='pagos_update'),
    path('pagos/delete/<int:pk>/', PagosDeleteView.as_view(), name='pagos_delete'),
]
