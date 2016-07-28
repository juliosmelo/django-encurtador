# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-26 23:12
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('full_url', models.URLField(verbose_name='URL')),
                ('counter', models.PositiveIntegerField(default=0, verbose_name='Contador')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
            ],
        ),
    ]