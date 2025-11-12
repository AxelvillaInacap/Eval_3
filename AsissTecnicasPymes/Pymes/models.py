from django.db import models


def obtener_digito_verificador(rut):
        rut = rut[::-1] # Invierte el RUT
        suma = 0
        multiplicador = 2
        for digito in rut:
            suma += int(digito) * multiplicador
            multiplicador += 1
            if multiplicador == 8:
                multiplicador = 2
        
        resto = suma % 11
        if resto == 0:
            return "0"
        elif resto == 1:
            return "K"
        else:
            return str(11 - resto)

def es_valido(rut):
        try:
            # Limpiar el RUT de puntos y guiones
            rut = "".join(c for c in rut if c.isalnum())
            if len(rut) < 2:
                return False

            numero_str = rut[:-1]
            dv_ingresado = rut[-1].upper()

            dv_calculado = obtener_digito_verificador(numero_str)

            return dv_ingresado == dv_calculado
        except Exception as e:
            return False
class Empresa(models.Model):
    rut = models.CharField(unique=True, max_length=10)
    razon_social = models.CharField(max_length=100, blank=False)
    giro = models.CharField(max_length=100)
    telefono = models.CharField(max_length=9)
    email = models.EmailField(max_length=30)
    direccion = models.CharField(max_length=40)
    comuna = models.CharField(max_length=40)

    if es_valido(rut):
        raise ValueError("El RUT ingresado no es válido.")

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