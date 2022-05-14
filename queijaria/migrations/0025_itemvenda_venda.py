# Generated by Django 4.0.4 on 2022-05-11 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('queijaria', '0024_alter_cliente_content_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemVenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.FloatField()),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='queijaria.produto')),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('total', models.FloatField()),
                ('faturamento', models.CharField(max_length=25)),
                ('vencimento', models.DateField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='queijaria.cliente')),
                ('items', models.ManyToManyField(to='queijaria.itemvenda')),
            ],
        ),
    ]
