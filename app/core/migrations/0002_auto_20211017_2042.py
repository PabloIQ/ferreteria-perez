# Generated by Django 3.2.7 on 2021-10-18 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto',
            name='url1',
            field=models.ImageField(default='null', upload_to='imagenes', verbose_name='Miniatura'),
        ),
        migrations.AlterField(
            model_name='foto',
            name='url2',
            field=models.ImageField(default='null', upload_to='imagenes', verbose_name='Miniatura'),
        ),
        migrations.AlterField(
            model_name='foto',
            name='url3',
            field=models.ImageField(default='null', upload_to='imagenes', verbose_name='Miniatura'),
        ),
    ]
