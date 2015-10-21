# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usertw', models.TextField(verbose_name='UserTw', blank=True)),
                ('text', models.TextField(null=True, verbose_name='Tweet', blank=True)),
                ('keywords', models.TextField(null=True, verbose_name='Keywords', blank=True)),
                ('sentiment', models.TextField(null=True, verbose_name='Setiment', blank=True)),
                ('created_tw', models.DateTimeField(verbose_name='fecha tweet', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserTw',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('screen_name', models.CharField(max_length=50, verbose_name='Screen name')),
                ('screen_id', models.CharField(unique=True, max_length=100, verbose_name='Id', blank=True)),
                ('description', models.TextField(null=True, verbose_name='Description', blank=True)),
                ('timeline', models.TextField(null=True, verbose_name='Timeline', blank=True)),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='fecha ingreso', blank=True)),
                ('personality', models.TextField(null=True, verbose_name='Personality', blank=True)),
                ('challenge', models.TextField(null=True, verbose_name='challenge', blank=True)),
                ('closeness', models.TextField(null=True, verbose_name='closeness', blank=True)),
                ('curiosity', models.TextField(null=True, verbose_name='curiosity', blank=True)),
                ('excitement', models.TextField(null=True, verbose_name='excitement', blank=True)),
                ('harmony', models.TextField(null=True, verbose_name='harmony', blank=True)),
                ('ideal', models.TextField(null=True, verbose_name='ideal', blank=True)),
                ('liberty', models.TextField(null=True, verbose_name='liberty', blank=True)),
                ('love', models.TextField(null=True, verbose_name='love', blank=True)),
                ('practicality', models.TextField(null=True, verbose_name='practicality', blank=True)),
                ('selfexpression', models.TextField(null=True, verbose_name='selfexpression', blank=True)),
                ('stability', models.TextField(null=True, verbose_name='stability', blank=True)),
                ('structure', models.TextField(null=True, verbose_name='structure', blank=True)),
            ],
        ),
    ]
