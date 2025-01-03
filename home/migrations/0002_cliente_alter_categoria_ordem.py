# Generated by Django 4.2.16 on 2024-12-16 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cliente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                ("cpf", models.CharField(max_length=15, verbose_name="C.P.F")),
                ("datanasc", models.DateField(verbose_name="Data de Nascimento")),
            ],
        ),
        migrations.AlterField(
            model_name="categoria",
            name="ordem",
            field=models.PositiveIntegerField(unique=True),
        ),
    ]
