from django.db import models
from django.forms import model_to_dict

# Create your models here.
class Estudiante(models.Model):
    dniEstudiante = models.IntegerField(unique=True, primary_key=True)
    nombre = models.CharField(max_length=50, verbose_name='Nombres')
    apellidoPaterno = models.CharField(max_length=35, verbose_name='Apellido Paterno')
    apellidoMaterno = models.CharField(max_length=35, verbose_name='Apellido Materno')
    fechaNacimiento = models.DateField()
    numeroCelular = models.IntegerField(verbose_name='Número de Celular')
    correoEle = models.CharField(max_length=35, verbose_name='Correo Electrónico')
    departamento = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'

    def nombreCompleto(self):
        txt = "{0} {1}, {2}"
        return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombre)

    def __str__(self):
        txt = "{0}/ DNI: {1}"
        return txt.format(self.nombreCompleto(),self.dniEstudiante)
    
        
    def toJSON(self):
        item = model_to_dict(self)
        item['nombrecompleto'] = self.nombreCompleto()
        return item

# Create your models here.
class Profesores(models.Model):
    dniProfesor = models.IntegerField(unique=True, primary_key=True)
    nombre = models.CharField(max_length=50, verbose_name='Nombres')
    apellidoPaterno = models.CharField(max_length=35, verbose_name='Apellido Paterno')
    apellidoMaterno = models.CharField(max_length=35, verbose_name='Apellido Materno')
    idioma= models.CharField(max_length=35, verbose_name='Idioma a enseñar')
    fechaNacimiento = models.DateField()
    numeroCelular = models.IntegerField(verbose_name='Número de Celular')
    correoEle = models.CharField(max_length=35, verbose_name='Correo Electrónico')
    sueldo = models.IntegerField(verbose_name='Sueldo Mensual')

    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'
    
    def nombreCompleto(self):
        txt = "{0} {1}, {2}"
        return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombre)

    def __str__(self):
        txt = "{0}/ DNI: {1}/ {2}"
        return txt.format(self.nombreCompleto(),self.dniProfesor, self.idioma)

    def toJSON(self):
        item = model_to_dict(self)
        item['nombrecompleto'] = self.nombreCompleto()
        return item

class Niveles(models.Model):
    id = models.AutoField(primary_key=True)
    IDnivel = models.CharField(max_length=30, verbose_name='ID del Nivel')
    modalidad = models.CharField(max_length=35, verbose_name='Modalidad')
    opciones_nivel = [
        ("B1", "Básico 1"),
        ("B2", "Básico 2"),
        ("B3", "Básico 3"),
        ("I1", "Intermedio 1"),
        ("I2", "Intermedio 2"),
        ("A", "Avanzado"),
    ]
    nivel = models.CharField(max_length=2, choices=opciones_nivel, default="B1")
    frecuencia = models.CharField(max_length=35, verbose_name='Frecuencia')
    horario = models.CharField(max_length=35, verbose_name='Horario')

    class Meta:
        verbose_name = 'Nivel'
        verbose_name_plural = 'Niveles'
    def __str__(self):
        txt = "{0}"
        return txt.format(self.IDnivel)
    def toJSON(self):
        item = model_to_dict(self)
        return item

class PagoNivel(models.Model):
    id = models.AutoField(primary_key=True)
    fechapago = models.DateField()
    DNIestudiante= models.ForeignKey("Estudiante", verbose_name="DNI Estudiante", on_delete=models.CASCADE)
    DNIprofesor = models.ForeignKey("Profesores", verbose_name="DNI Profesor", on_delete=models.CASCADE)
    Idnivel= models.ForeignKey("Niveles", verbose_name="ID del Nivel", on_delete=models.CASCADE)
    Mesnivel = models.CharField(max_length=15, verbose_name='Mes de nivel')
    Añonivel = models.CharField(max_length=15, verbose_name='Año de nivel')
    precio = models.CharField(max_length=15, verbose_name='Precio')
    metodopago = models.CharField(max_length=15, verbose_name='Metodo de pago')

    class Meta:
        verbose_name ="Pago"
        verbose_name_plural ="Pagos"

    def __str__(self):
        return self.name
    
    def DatEstu(self):
        txt = "{0} {1} {2}/DNI: {3}"
        return txt.format(self.DNIestudiante.apellidoPaterno, self.DNIestudiante.apellidoMaterno, self.DNIestudiante.nombre, self.DNIestudiante.dniEstudiante)
    def DatProf(self):
        txt = "{0} {1} {2}/DNI: {3}"
        return txt.format(self.DNIprofesor.apellidoPaterno, self.DNIprofesor.apellidoMaterno, self.DNIprofesor.nombre, self.DNIprofesor.dniProfesor)
    def toJSON(self):
        item = model_to_dict(self)
        item['DNIestudiante'] = self.DatEstu()
        item['DNIprofesor'] = self.DatProf()
        item['Idnivel'] = self.Idnivel.IDnivel

        return item
