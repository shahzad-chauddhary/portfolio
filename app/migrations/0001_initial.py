# Generated by Django 2.2.4 on 2020-04-23 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MobileApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='gallery')),
            ],
        ),
        migrations.CreateModel(
            name='WorkDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=15)),
                ('category', models.CharField(max_length=15)),
                ('project_date', models.DateField()),
                ('banner_img', models.ImageField(upload_to='details')),
                ('descrip_1', models.CharField(max_length=250)),
                ('descrip_2', models.CharField(max_length=250)),
                ('thumb_img1', models.ImageField(upload_to='details')),
                ('thumb_img2', models.ImageField(upload_to='details')),
            ],
        ),
    ]
