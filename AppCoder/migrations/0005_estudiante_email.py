# Generated by Django 4.1.5 on 2023-02-05 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0004_curso_entregable'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
    ]
