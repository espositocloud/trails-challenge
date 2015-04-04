# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import challenge.validators
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Patrol',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('hour_condition', models.BooleanField(default=True)),
                ('group', models.ForeignKey(related_name='patrols', to='challenge.Group')),
            ],
            options={
                'ordering': ('group', 'name'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Technique',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('radio_id', models.CharField(max_length=20, blank=True)),
                ('name', models.CharField(max_length=100)),
                ('person_name', models.CharField(max_length=100, blank=True)),
                ('phone', models.CharField(max_length=30, blank=True)),
                ('note', models.CharField(max_length=200, blank=True)),
                ('check_condition', models.BooleanField(default=False)),
                ('staff', models.ForeignKey(related_name='techniques', to='challenge.Group', null=True)),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('technique_score', models.IntegerField(validators=[challenge.validators.validate_score])),
                ('style_score', models.IntegerField(validators=[challenge.validators.validate_score])),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, auto_now_add=True)),
                ('modified_date', models.DateTimeField(default=django.utils.timezone.now, auto_now=True)),
                ('user', models.CharField(max_length=50, null=True, blank=True)),
                ('patrol', models.ForeignKey(related_name='tests', to='challenge.Patrol')),
                ('technique', models.ForeignKey(related_name='tests', to='challenge.Technique')),
            ],
            options={
                'ordering': ('-created_date',),
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='test',
            unique_together=set([('patrol', 'technique')]),
        ),
    ]
