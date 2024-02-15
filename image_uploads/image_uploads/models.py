from django.db import models

class store(models.Model):
    name = models.CharField(max_length=220)
    image = models.ImageField(upload_to='image_uploads/files')
    