# Generated by Django 4.0.3 on 2022-09-14 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Counts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SERVIDOR', models.CharField(max_length=255)),
                ('CAMARA', models.CharField(max_length=255)),
                ('JUNIO', models.CharField(max_length=255)),
                ('JULIO', models.CharField(max_length=255)),
                ('AGOSTO', models.CharField(max_length=255)),
                ('SEPTIEMBRE', models.CharField(max_length=255)),
                ('OCTUBRE', models.CharField(max_length=255)),
                ('NOVIEMBRE', models.CharField(max_length=255)),
                ('DICIEMBRE', models.CharField(max_length=255)),
                ('ENERO', models.CharField(max_length=255)),
                ('FEBRERO', models.CharField(max_length=255)),
                ('MARZO', models.CharField(max_length=255)),
                ('ABRIL', models.CharField(max_length=255)),
                ('MAYO', models.CharField(max_length=255)),
                ('OTROS', models.CharField(max_length=255)),
                ('VIDEOS', models.CharField(max_length=255)),
                ('MULTAS', models.CharField(max_length=255)),
            ],
        ),
    ]