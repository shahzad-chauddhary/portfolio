from django.db import models


class MobileApp(models.Model):
    img = models.ImageField(upload_to='gallery')
