# Generated by Django 2.2 on 2019-04-22 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_auto_20190413_0023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_doc', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='doc',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.Documento'),
        ),
    ]