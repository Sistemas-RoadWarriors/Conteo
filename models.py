from django.db import models


# Create your models here.
class Counts(models.Model):
    # id = models.CharField(max_length=255, primary_key=True)
    SERVIDOR = models.CharField(max_length=255)
    CAMARA = models.CharField(max_length=255)
    JUNIO = models.CharField(max_length=255)
    JULIO = models.CharField(max_length=255)
    AGOSTO = models.CharField(max_length=255)
    SEPTIEMBRE = models.CharField(max_length=255)
    NOVIEMBRE = models.CharField(max_length=255)
    OCTUBRE = models.CharField(max_length=255)
    DICIEMBRE = models.CharField(max_length=255)
    ENERO = models.CharField(max_length=255)
    FEBRERO = models.CharField(max_length=255)
    MARZO = models.CharField(max_length=255)
    ABRIL = models.CharField(max_length=255)
    MAYO = models.CharField(max_length=255)
    VIDEOS = models.CharField(max_length=255)
    MULTAS = models.CharField(max_length=255)

#    return f'Conteo {self.id}: {self.SERVIDOR} {self.CAMARA} {self.NOVIEMBRE} {self.OTROS} {self.VIDEOS}'
