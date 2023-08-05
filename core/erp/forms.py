from django.forms import *

from core.erp.models import Estudiante, Profesores, Niveles, PagoNivel


class EstudianteForm(ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'
        widgets = {
            'dniEstudiante': TextInput(attrs={'placeholder': 'Ingrese DNI'}),
            'nombre': TextInput(attrs={'placeholder': 'Ingrese nombres'}),
            'apellidoPaterno': TextInput(attrs={'placeholder': 'Ingrese apellido paterno'}),
            'apellidoMaterno': TextInput(attrs={'placeholder': 'Ingrese apellido materno'}),
            'fechaNacimiento': DateInput(attrs={'placeholder': 'Ingrese fecha de nacimiento', 'type': 'date'}),
            'numeroCelular': TextInput(attrs={'placeholder': 'Ingrese número celular'}),
            'correoEle': EmailInput(attrs={'placeholder': 'Ingrese correo electrónico'}),
            'departamento': TextInput(attrs={'placeholder': 'Ingrese región'}),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class ProfesoresForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dniProfesor'].widget.attrs['autofocus'] = True

    class Meta:
        model = Profesores
        fields = '__all__'
        widgets = {
            'dniProfesor': TextInput(attrs={'placeholder': 'Ingrese DNI'}),
            'nombre': TextInput(attrs={'placeholder': 'Ingrese nombres'}),
            'apellidoPaterno': TextInput(attrs={'placeholder': 'Ingrese apellido paterno'}),
            'apellidoMaterno': TextInput(attrs={'placeholder': 'Ingrese apellido materno'}),
            'fechaNacimiento': TextInput(attrs={'placeholder': 'Ingrese fecha de nacimiento', 'type': 'date'}),
            'numeroCelular': TextInput(attrs={'placeholder': 'Ingrese número celular'}),
            'correoEle': EmailInput(attrs={'placeholder': 'Ingrese correo electrónico'}),
            'sueldo': TextInput(attrs={'placeholder': 'Ingrese sueldo'}),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
    
class NivelesForm(ModelForm):
    
    class Meta:
        model = Niveles
        fields = '__all__'
        widgets = {
            'horario': TextInput(attrs={'placeholder': 'Ingrese horario'}),
            'frecuencia': TextInput(attrs={'placeholder': 'Ingrese frecuencia'}),
            'docente': Select(attrs={'placeholder': 'Seleccione docente'}),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
    
class PagoNivelForm(ModelForm):
    DNIestudiante = ModelChoiceField(
        label="DNI del Estudiante",
        queryset=Estudiante.objects.all(),
        widget=Select(attrs={'class': 'form-control select2', 'style': 'width: 100%'})
    )
    DNIprofesor = ModelChoiceField(
        label="DNI del Profesor",
        queryset=Profesores.objects.all(),
        widget=Select(attrs={'class': 'form-control select2', 'style': 'width: 100%'})
    )
    Idnivel = ModelChoiceField(
        label="ID del Nivel",
        queryset=Niveles.objects.all(),
        widget=Select(attrs={'class': 'form-control select2', 'style': 'width: 100%'})
    )

    class Meta:
        model = PagoNivel
        fields = '__all__'
        widgets = {
            'IDPagonivel': TextInput(attrs={'placeholder': 'Ingrese ID del pago'}),
            'fechapago': DateInput(attrs={'placeholder': 'Ingrese fecha de matrícula', 'type': 'date'}),
            'Mesnivel': TextInput(attrs={'placeholder': 'Ingrese mes de nivel'}),
            'Añonivel': TextInput(attrs={'placeholder': 'Ingrese año de nivel'}),
            'precio': TextInput(attrs={'placeholder': 'Ingrese precio'}),
            'metodopago': TextInput(attrs={'placeholder': 'Ingrese metodo de pago'}),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
    