# Generated by Django 5.0.3 on 2024-05-07 10:42

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admKombustivel', '0004_senhas_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='DistribuitorRelatorio',
            fields=[
                ('id_distribuitor', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('naran_distribuitor', models.CharField(max_length=200)),
                ('montante_distribuitor', models.FloatField(default=0)),
                ('data', models.DateField(default=datetime.date.today)),
                ('ano', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admKombustivel.tinan')),
            ],
        ),
    ]