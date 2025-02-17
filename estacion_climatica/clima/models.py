from django.db import models

# Create your models here.


class DatosClimaticos(models.Model):
    fecha = models.DateField()
    temperatura = models.FloatField()
    humedad = models.FloatField()
    luz = models.FloatField()
    presion = models.FloatField()

    class Meta:
        db_table = 'datos_climaticos' 