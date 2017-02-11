# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 21:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('log_reg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('all_users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_products', to='log_reg.User')),
                ('user_products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_of_user', to='log_reg.User')),
            ],
        ),
    ]
