# Generated by Django 4.2.16 on 2024-10-04 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("high_level", "0008_recette_recetteingredient_recette_ingredients"),
    ]

    operations = [
        migrations.AddField(
            model_name="usine",
            name="ressources",
            field=models.ManyToManyField(blank=True, to="high_level.ressource"),
        ),
    ]
