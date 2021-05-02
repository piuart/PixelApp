from django.db import models
from ckeditor.fields import RichTextField



class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre de la categoria', max_length=100, null=False, blank=False)
    creation_date = models.DateField('Fecha de creacion', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Titulo', max_length=90, blank=False, null=False)
    description = models.CharField('Descripcion', max_length=110, blank=False, null=False)
    contents = RichTextField(verbose_name = "Contenido del post")
    image = models.ImageField(verbose_name = "Imagen", upload_to = "post")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ["-created"]
    
    def __str__(self):
        return self.title