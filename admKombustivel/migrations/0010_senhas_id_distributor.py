# Generated by Django 5.0.4 on 2024-06-11 00:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admKombustivel', '0009_alter_distribuisaun_id_transporte'),
    ]

    operations = [
        migrations.AddField(
            model_name='senhas',
            name='id_distributor',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='admKombustivel.distribuitor'),
            preserve_default=False,
        ),
    ]