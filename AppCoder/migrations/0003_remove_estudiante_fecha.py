# Generated by Django 4.1.5 on 2023-01-26 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_profesor_edad_alter_estudiante_comision'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiante',
            name='fecha',
        ),
    ]
