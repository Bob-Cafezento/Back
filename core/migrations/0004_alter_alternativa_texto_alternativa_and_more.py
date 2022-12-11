# Generated by Django 4.1.4 on 2022-12-10 23:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("core", "0003_remove_alternativa_texto_alternativas_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="alternativa",
            name="texto_alternativa",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="conteudo",
            name="criado_por",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="conteudos",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]