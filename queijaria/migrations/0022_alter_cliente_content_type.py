# Generated by Django 4.0.4 on 2022-05-11 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('queijaria', '0021_alter_cliente_content_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='content_type',
            field=models.ForeignKey(limit_choices_to=models.Q(('model', 'pessoafisica')), on_delete=django.db.models.deletion.DO_NOTHING, to='contenttypes.contenttype'),
        ),
    ]
