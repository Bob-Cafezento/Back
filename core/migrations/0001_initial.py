# Generated by Django 4.1.4 on 2022-12-08 04:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Alternativa",
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
                ("texto_alternativas", models.CharField(max_length=150)),
                ("esta_correta", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Conteudo",
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
                ("nome", models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name="Disciplina",
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
                ("nome", models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name="Pergunta",
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
                ("texto_pergunta", models.CharField(max_length=150)),
                (
                    "alternativas",
                    models.ManyToManyField(related_name="+", to="core.alternativa"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Formulario",
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
                (
                    "titulo",
                    models.CharField(
                        default="New Form", max_length=255, verbose_name="Form Title"
                    ),
                ),
                ("data_criacao", models.DateTimeField(auto_now_add=True)),
                (
                    "conteudo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="core.conteudo",
                    ),
                ),
                (
                    "criado_por",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="formularios",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "perguntas",
                    models.ManyToManyField(related_name="+", to="core.pergunta"),
                ),
            ],
        ),
        migrations.AddField(
            model_name="conteudo",
            name="disciplina",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="conteudos",
                to="core.disciplina",
            ),
        ),
    ]
