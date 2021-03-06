# Generated by Django 2.2.1 on 2019-06-08 19:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serve', '0003_aula_curso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='Assunto',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='aula',
            name='Data',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='Description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='EndDate',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='StartDate',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='EndDate',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='StartDate',
            field=models.DateField(blank=True, default=datetime.date(2019, 6, 8)),
        ),
        migrations.AlterField(
            model_name='turma',
            name='Description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='turma',
            name='EndTime',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='turma',
            name='StartTime',
            field=models.TimeField(blank=True),
        ),
    ]
