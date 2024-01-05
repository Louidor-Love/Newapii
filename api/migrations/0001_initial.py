# Generated by Django 4.2.9 on 2024-01-03 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('tipo_de_cambio', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'cotizaciones',
            },
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_de_compra', models.DateField()),
                ('cotizacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cotizacion')),
            ],
            options={
                'db_table': 'compras',
            },
        ),
    ]