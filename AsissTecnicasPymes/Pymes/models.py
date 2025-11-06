from django.db import models

class Empresa(models.Model):
    rut = models.CharField(unique=True, max_length=10)
    razon_social = models.CharField(max_length=100, blank=False)
    giro = models.CharField(max_length=100)
    telefono = models.CharField(max_length=9)
    email = models.EmailField(max_length=30)
    direccion = models.CharField(max_length=40)
    comuna = models.CharField(max_length=40)

    def __str__(self):
        return self.razon_social

class Servicio(models.Model):
    nombre = models.CharField(unique=True, max_length=30)
    descripcion = models.CharField(max_length=200)
    categoria = models.CharField(choices=[('diagnostico', 'Diagnóstico'), ('prototipo', 'Prototipo'), ('automatización', 'Automatización')], max_length=30)
    dur_est_horas = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Profesional(models.Model):
    run = models.CharField(unique=True, max_length=10)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

class OrdenServicio(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)
    estado = models.CharField(choices=[('nueva', 'Nueva'), ('en_ejecucion', 'En Ejecución'), ('finalizada', 'Finalizada'), ('cancelada', 'Cancelada')], max_length=30, null=False, blank=False)
    prioridad = models.CharField(choices=[('baja', 'Baja'), ('media', 'Media'), ('alta', 'Alta')], max_length=30, null=False, blank=False)
    des_requerimiento = models.CharField(max_length=100)
    ser_seleccionados = models.ManyToManyField(Servicio)
    pro_asignado = models.ForeignKey(Profesional, on_delete=models.SET_NULL, null=True, blank=True)
    
    def tareas(self):
        if self.estado == 'finalizada':
            print(f"Orden {self.id} finalizada. No hay tareas pendientes")
            self.save()
        
    def __str__(self):
        return f"Orden {self.id} - {self.empresa.razon_social}"