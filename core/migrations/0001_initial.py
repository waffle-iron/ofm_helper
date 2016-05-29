# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-29 17:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.IntegerField(choices=[(1, 'Ägypten'), (2, 'Bosnien und Herzegowina'), (3, 'Brasilien'), (4, 'Deutschland'), (5, 'England'), (6, 'Frankreich'), (7, 'Italien'), (8, 'Kuba'), (9, 'Neuseeland'), (10, 'Norwegen'), (11, 'Österreich'), (12, 'San Marino'), (13, 'Spanien'), (14, 'Türkei'), (15, 'Thailand'), (16, 'Ukraine')])),
            ],
        ),
        migrations.CreateModel(
            name='CurrentMatchday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('league', models.IntegerField(choices=[(1, '1. Liga'), (2, '2. Liga'), (3, 'Regionalliga'), (4, 'Oberliga'), (5, 'Verbandsliga'), (6, 'Landesliga'), (7, 'Landesklasse'), (8, 'Bezirksliga'), (9, 'Bezirksklasse'), (10, 'Kreisliga'), (11, 'Kreisklasse')])),
                ('relay', models.CharField(max_length=10)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Matchday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matchday', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Quarter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quarter', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')])),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='quarter',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Season'),
        ),
        migrations.AddField(
            model_name='matchday',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Season'),
        ),
        migrations.AddField(
            model_name='currentmatchday',
            name='matchday',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Matchday'),
        ),
    ]