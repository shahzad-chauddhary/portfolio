from django.db import models


class MobileApp(models.Model):
    img = models.ImageField(upload_to='gallery')

class WorkDetail(models.Model):
    client_name = models.CharField(max_length=15)
    category = models.CharField(max_length=15)
    project_date = models.DateField()
    banner_img = models.ImageField(upload_to='details')
    descrip_1 = models.CharField(max_length=250)
    descrip_2 = models.CharField(max_length=250)
    thumb_img1 = models.ImageField(upload_to='details')
    thumb_img2 = models.ImageField(upload_to='details')
