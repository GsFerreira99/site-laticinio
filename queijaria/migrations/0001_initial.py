# Generated by Django 4.0.4 on 2022-05-15 03:19

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(limit_choices_to=models.Q(('model', 'pessoafisica'), ('model', 'pessoajuridica'), _connector='OR'), on_delete=django.db.models.deletion.DO_NOTHING, to='contenttypes.contenttype')),
            ],
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('endereco', models.CharField(blank=True, max_length=200)),
                ('telefone', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('sobrenome', models.CharField(max_length=50)),
                ('cpf', models.CharField(max_length=11)),
                ('nascimento', models.DateField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PessoaJuridica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('endereco', models.CharField(blank=True, max_length=200)),
                ('telefone', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('razao_social', models.CharField(max_length=255)),
                ('cnpj', models.CharField(max_length=14)),
                ('inscricao_estadual', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TipoProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
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
                ('status', models.CharField(default='Em Aberto', max_length=20)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='queijaria.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='RecebimentoLeite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField()),
                ('quantidade', models.FloatField(default=0)),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='queijaria.fornecedor')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40, unique=True)),
                ('marca', models.CharField(default=0, max_length=25)),
                ('codBarras', models.IntegerField(default=0)),
                ('valorCompra', models.FloatField(default=0)),
                ('valorVenda', models.FloatField(default=0)),
                ('categoria', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='queijaria.categoriaproduto')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='queijaria.tipoproduto')),
            ],
            options={
                'default_related_name': 'produto',
            },
        ),
        migrations.CreateModel(
            name='Producao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('leite', models.IntegerField()),
                ('sal', models.FloatField(blank=True, default=0)),
                ('peso', models.FloatField(blank=True, default=0)),
                ('rendimento', models.FloatField(blank=True, default=0)),
                ('acucar', models.FloatField(blank=True, default=0)),
                ('lote', models.IntegerField()),
                ('observacao', models.TextField(blank=True)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='queijaria.produto')),
            ],
            options={
                'default_related_name': 'producao',
            },
        ),
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.FloatField(default=0)),
                ('unidade', models.CharField(max_length=20)),
                ('produto', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='queijaria.produto')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('cpf', models.IntegerField(default=0)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
