# Generated by Django 2.2.7 on 2019-11-16 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leche',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100)),
                ('FechaVencimiento', models.DateField()),
                ('Cantidad', models.IntegerField()),
                ('Lote', models.CharField(max_length=20)),
            ],
        ),
    ]