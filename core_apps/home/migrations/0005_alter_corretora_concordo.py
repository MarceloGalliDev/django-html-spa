# Generated by Django 5.0.6 on 2024-06-24 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_alter_corretora_cnpj"),
    ]

    operations = [
        migrations.AlterField(
            model_name="corretora",
            name="concordo",
            field=models.BooleanField(default=True, verbose_name="Concordo"),
        ),
    ]