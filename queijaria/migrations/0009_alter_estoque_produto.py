# Generated by Django 4.0.4 on 2022-05-10 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('queijaria', '0008_alter_estoque_produto_alter_produto_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estoque',
            name='produto',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='queijaria.produto'),
        ),
    ]
