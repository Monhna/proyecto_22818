# Generated by Django 3.2.14 on 2022-11-15 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cac', '0005_auto_20221115_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiantem',
            name='baja',
            field=models.BooleanField(default=0),
        ),
    ]