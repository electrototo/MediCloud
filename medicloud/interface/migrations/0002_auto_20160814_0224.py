# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('interface', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='baseUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_of_user', models.CharField(max_length=20)),
                ('attached', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='doctorExtent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('basicInformation', models.CharField(max_length=400)),
                ('doctor', models.OneToOneField(to='interface.baseUser')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='patientExtent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=30, blank=True)),
                ('ocupation', models.CharField(max_length=500, blank=True)),
                ('height', models.FloatField(blank=True)),
                ('weight', models.FloatField(blank=True)),
                ('blood', models.CharField(max_length=500, blank=True)),
                ('alergies', models.CharField(max_length=500, blank=True)),
                ('diagnostic', models.CharField(max_length=500, blank=True)),
                ('responsible', models.EmailField(max_length=75, blank=True)),
                ('doctor', models.ManyToManyField(to='interface.doctorExtent', blank=True)),
                ('meds', models.ManyToManyField(to='interface.Meds', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='medic',
            name='userAttached',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='medicOnDuty',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='meds',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='userAttached',
        ),
        migrations.DeleteModel(
            name='patient',
        ),
        migrations.RemoveField(
            model_name='meds',
            name='assignedBy',
        ),
        migrations.DeleteModel(
            name='Medic',
        ),
        migrations.RemoveField(
            model_name='meds',
            name='dosis',
        ),
        migrations.RemoveField(
            model_name='meds',
            name='hour_frequency',
        ),
        migrations.RemoveField(
            model_name='meds',
            name='startDate',
        ),
        migrations.AddField(
            model_name='meds',
            name='beginDate',
            field=models.DateField(default=datetime.datetime(2016, 8, 14, 2, 24, 4, 505817, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meds',
            name='instructions',
            field=models.CharField(max_length=500, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='meds',
            name='lapse',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='meds',
            name='endDate',
            field=models.DateField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meds',
            name='name',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
    ]
