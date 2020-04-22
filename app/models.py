from django.db import models


class MobileApp(models.Model):
    img = models.ImageField(upload_to='gallery')

class WorkDetail(models.Model):
    clientnam = models.CharField(max_length=15)
    category = models.CharField(max_length=15)
    proj_date = models.DateField()
    cimg = models.ImageField(upload_to='details')
    des1 = models.CharField(max_length=150)
    des2 = models.CharField(max_length=150)
    thumb_img1 = models.ImageField(upload_to='details')
    thumb_img2 = models.ImageField(upload_to='details')
