# Generated by Django 5.1.2 on 2024-11-03 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrum', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tarea',
            options={'permissions': [('puede_completar_tarea', 'Puede completar tarea')]},
        ),
    ]
