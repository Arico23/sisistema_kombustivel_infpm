# Generated by Django 5.0.3 on 2024-05-13 14:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admKombustivel', '0008_alter_distribuisaun_id_transporte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distribuisaun',
            name='id_transporte',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admKombustivel.transporte'),
        ),
    ]
