# Generated by Django 5.0.6 on 2024-06-23 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_alter_corretora_telefone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="corretora",
            name="telefone",
            field=models.CharField(max_length=15, verbose_name="Telefone"),
        ),
    ]