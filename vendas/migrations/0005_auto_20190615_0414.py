# Generated by Django 2.2 on 2019-06-15 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0004_auto_20190614_2122'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='venda',
            options={'permissions': (('setar_nfe', 'Usuario pode setar NF-e'), ('ver_dashboard', 'Pode visualizar dashboard'), ('permissão_3', 'Permissão 3'))},
        ),
    ]
