# Generated by Django 5.1.2 on 2024-11-02 18:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre descriptivo del Sprint', max_length=100, verbose_name='Nombre del Sprint')),
                ('objetivo', models.TextField(blank=True, null=True)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('velocidad', models.IntegerField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now_add=True)),
                ('equipo_de_desarrollo', models.ManyToManyField(blank=True, related_name='sprint_como_desarrollador', to=settings.AUTH_USER_MODEL)),
                ('scrum_master', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sprint_como_scrum_master', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(help_text='Un titulo que describa la tarea.', max_length=200, verbose_name='Titulo de la Tarea')),
                ('descripcion', models.TextField(blank=True)),
                ('criterios_aceptacion', models.TextField(blank=True, null=True)),
                ('prioridad', models.CharField(choices=[('BAJA', 'Baja'), ('MEDIA', 'Media'), ('ALTA', 'Alta')], default='BAJA', max_length=10)),
                ('estado', models.CharField(choices=[('POR_HACER', 'Por Hacer'), ('EN_PROGRESO', 'En Progreso'), ('COMPLETADA', 'Completada')], default='POR_HACER', max_length=20)),
                ('esfuerzo_estimado', models.IntegerField(blank=True, null=True)),
                ('fecha_de_creacion', models.DateTimeField(auto_now=True)),
                ('fecha_de_actualizacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_de_finalizacion', models.DateTimeField(blank=True, null=True)),
                ('bloqueadores', models.TextField(blank=True, null=True)),
                ('dependencias', models.ManyToManyField(blank=True, to='scrum.tarea')),
                ('responsable', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('sprint_asignado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='scrum.sprint')),
            ],
        ),
        migrations.AddField(
            model_name='sprint',
            name='backlog_sprint',
            field=models.ManyToManyField(blank=True, related_name='sprint_backlog', to='scrum.tarea'),
        ),
        migrations.CreateModel(
            name='Epica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre descriptivo de la Epica.', max_length=200, verbose_name='Nombre de la Epica')),
                ('descripcion', models.TextField()),
                ('criterios_aceptacion', models.TextField()),
                ('estado', models.CharField(choices=[('POR_HACER', 'Por Hacer'), ('EN_PROGRESO', 'En Progreso'), ('COMPLETADA', 'Completada')], default='POR_HACER', max_length=20)),
                ('esfuerzo_estimado_total', models.IntegerField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('progreso', models.FloatField()),
                ('dependencias', models.ManyToManyField(blank=True, to='scrum.epica')),
                ('responsable', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('tareas_asociadas', models.ManyToManyField(blank=True, related_name='epicas_tareas', to='scrum.tarea')),
            ],
        ),
        migrations.AddConstraint(
            model_name='tarea',
            constraint=models.CheckConstraint(condition=models.Q(('estado', 'POR_HACER'), ('estado', 'EN_PROGRESO'), ('estado', 'COMPLETADA'), _connector='OR'), name='estado_valido_tarea'),
        ),
        migrations.AddConstraint(
            model_name='tarea',
            constraint=models.CheckConstraint(condition=models.Q(('prioridad', 'BAJA'), ('prioridad', 'MEDIA'), ('prioridad', 'ALTA'), _connector='OR'), name='prioridad_valido_tarea'),
        ),
        migrations.AddConstraint(
            model_name='tarea',
            constraint=models.CheckConstraint(condition=models.Q(('esfuerzo_estimado__gte', 0)), name='esfuerzo_estimado_no_negativo'),
        ),
        migrations.AddConstraint(
            model_name='tarea',
            constraint=models.CheckConstraint(condition=models.Q(('estado', 'COMPLETADA'), ('fecha_de_finalizacion__isnull', True), _connector='OR'), name='fecha_finalizacion_tarea'),
        ),
        migrations.AddConstraint(
            model_name='sprint',
            constraint=models.CheckConstraint(condition=models.Q(('velocidad__gte', 0)), name='velocidad_no_negativa'),
        ),
        migrations.AddConstraint(
            model_name='sprint',
            constraint=models.CheckConstraint(condition=models.Q(('fecha_fin__gte', models.F('fecha_inicio'))), name='fecha_fin_posterior'),
        ),
        migrations.AddConstraint(
            model_name='epica',
            constraint=models.CheckConstraint(condition=models.Q(('esfuerzo_estimado_total__gte', 0)), name='esfuerzo_total_no_negativo'),
        ),
        migrations.AddConstraint(
            model_name='epica',
            constraint=models.CheckConstraint(condition=models.Q(('progreso__gte', 0), ('progreso__lte', 1)), name='progreso_valido'),
        ),
        migrations.AddConstraint(
            model_name='epica',
            constraint=models.CheckConstraint(condition=models.Q(('estado', 'POR_HACER'), ('estado', 'EN_PROGRESO'), ('estado', 'COMPLETADA'), _connector='OR'), name='estado_valido_epica'),
        ),
        migrations.AddConstraint(
            model_name='epica',
            constraint=models.CheckConstraint(condition=models.Q(('fecha_fin__gte', models.F('fecha_inicio'))), name='fecha_fin_posterior_epica'),
        ),
    ]
