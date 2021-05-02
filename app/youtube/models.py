from django.db import models


from django.forms import model_to_dict
from six import python_2_unicode_compatible
import dateutil.parser
from django.db import models
from django.utils import timezone
from isodate import parse_duration

# Create your models here.



class ListaReproduccion(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=500, blank=True, null=True)
    descripcion = models.TextField(verbose_name='Descripción', blank=True, null=True)
    link_promo = models.URLField(null=True, blank=True, verbose_name="Promoción Url")
    idvideo = models.CharField(max_length=500, verbose_name='Id del Video')
    fecha_subida = models.DateField(blank=True, verbose_name='Fecha Ejecución', null=True)
    hora_subida = models.TimeField(blank=True, verbose_name='Hora Ejecución', null=True)
    visto = models.BooleanField(default=False)

    def fecha_subida_str(self):
        return str(self.fecha_subida)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    def __str__(self):
        return self.nombre

    class Meta:
        managed = True
        ordering = ['id']
