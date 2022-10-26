# Generated by Django 4.1.2 on 2022-10-21 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_remove_formulario_site"),
    ]

    operations = [
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
                ("topico", models.CharField(max_length=45)),
                ("paragrafo", models.TextField(max_length=255)),
                ("titulo", models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name="Midia",
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
                ("link", models.URLField(blank=True)),
                ("videos", models.FileField(blank=True, upload_to="")),
                ("imagens", models.ImageField(blank=True, upload_to="")),
                ("audios", models.FileField(blank=True, upload_to="")),
            ],
        ),
        migrations.DeleteModel(
            name="Responde",
        ),
        migrations.DeleteModel(
            name="Sel_res_form",
        ),
        migrations.RemoveField(
            model_name="resposta",
            name="textpresp",
        ),
        migrations.AddField(
            model_name="formulario",
            name="data_inicial",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="formulario",
            name="pergunta",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="formularios",
                to="core.pergunta",
            ),
        ),
        migrations.AddField(
            model_name="pergunta",
            name="resposta",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="perguntas",
                to="core.resposta",
            ),
        ),
        migrations.AddField(
            model_name="resposta",
            name="textoresp",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name="pergunta",
            name="texto_per",
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="conteudo",
            name="id_midia",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="conteudo",
                to="core.midia",
            ),
        ),
        migrations.AddField(
            model_name="pergunta",
            name="conteudo",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="perguntas",
                to="core.conteudo",
            ),
        ),
    ]