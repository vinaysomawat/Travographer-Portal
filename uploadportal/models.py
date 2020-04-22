from django.db import models

# Create your models here.

class Image(models.Model):
    Imagefile = models.FileField()
    uploaded_at = models.DateTimeField(auto_now_add=True)