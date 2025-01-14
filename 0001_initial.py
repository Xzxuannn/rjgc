# Generated by Django 3.2.25 on 2024-06-17 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species', models.CharField(max_length=50)),
                ('weight', models.FloatField()),
                ('length1', models.FloatField()),
                ('length2', models.FloatField()),
                ('length3', models.FloatField()),
                ('height', models.FloatField()),
                ('width', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='WaterQuality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(max_length=100)),
                ('monitoring_time', models.DateTimeField()),
                ('water_quality_category', models.CharField(max_length=10)),
                ('water_temperature', models.FloatField(blank=True, null=True)),
                ('pH', models.FloatField(blank=True, null=True)),
                ('dissolved_oxygen', models.FloatField(blank=True, null=True)),
                ('conductivity', models.FloatField(blank=True, null=True)),
                ('turbidity', models.FloatField(blank=True, null=True)),
                ('permanganate_index', models.FloatField(blank=True, null=True)),
                ('ammonia_nitrogen', models.FloatField(blank=True, null=True)),
                ('total_phosphorus', models.FloatField(blank=True, null=True)),
                ('total_nitrogen', models.FloatField(blank=True, null=True)),
                ('site_status', models.CharField(max_length=100)),
            ],
        ),
    ]
