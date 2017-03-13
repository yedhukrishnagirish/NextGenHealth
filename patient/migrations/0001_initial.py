# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-13 19:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('p_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('p_image', models.ImageField(upload_to='images/patients')),
                ('p_name', models.CharField(max_length=50)),
                ('p_age', models.IntegerField()),
                ('p_sx', models.CharField(max_length=10)),
                ('p_addr', models.CharField(max_length=100)),
                ('p_NoK', models.CharField(default='Nil', max_length=50)),
                ('p_blood', models.CharField(max_length=3)),
                ('p_contact', models.CharField(max_length=50)),
                ('p_allerg', models.CharField(default='Nil', max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
