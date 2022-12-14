# Generated by Django 4.1.1 on 2022-09-16 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SuperMarket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalle',
            name='Cat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='SuperMarket.categoria'),
        ),
        migrations.AddField(
            model_name='detalle',
            name='Prod',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='SuperMarket.producto'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='direccion',
            field=models.ManyToManyField(to='SuperMarket.direccion'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='direccion',
            field=models.ManyToManyField(to='SuperMarket.direccion'),
        ),
    ]
