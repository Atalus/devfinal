from django.db import models

# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=140)
    descripcion = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to="logos_cat")

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    nombre = models.CharField(max_length=140)
    descripcion = models.TextField(null=True,blank=True)
    pagina_web = models.URLField(max_length=200)
    logo = models.ImageField(upload_to="logos")
    categoria = models.ForeignKey(Categoria)
    direccion = models.CharField(max_length=255, null=True)
    latLng = models.CharField(max_length=120, null=True)

    def __str__(self):
        return self.nombre

class Startup(models.Model):
    nombre = models.CharField(max_length=140)
    descripcion = models.TextField(blank=True, null=True)
    pagina_web = models.URLField(max_length=200)
    logo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    proveedores = models.ManyToManyField(Proveedor)
    direccion = models.CharField(max_length=255, null=True)
    latLng = models.CharField(max_length=120, null=True)