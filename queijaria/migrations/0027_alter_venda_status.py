# Generated by Django 4.0.4 on 2022-05-15 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queijaria', '0026_venda_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='status',
            field=models.CharField(default='Em Aberto', max_length=20),
        ),
    ]
