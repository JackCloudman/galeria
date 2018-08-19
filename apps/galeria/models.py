from django.db import models
from django.utils import timezone
import hashlib,os
from tagging.fields import TagField

def update_filename(instance, filename):
    path = "img"
    fileName, fileExtension = os.path.splitext(filename)
    filename = filename+str(timezone.now())
    name = hashlib.sha256((filename).encode()).hexdigest()+fileExtension
    path  = os.path.join(path, name)
    return path

class Foto(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha = models.DateTimeField(default=timezone.now)
    src = models.ImageField(upload_to=update_filename)
    tags = TagField(null=True)

    def __str__(self):
        return self.titulo
