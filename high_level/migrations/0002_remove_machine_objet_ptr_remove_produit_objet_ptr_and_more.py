from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ("high_level", "0001_initial"),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name="machine",
        #     name="objet_ptr",
        # ),
        # migrations.RemoveField(
        #     model_name="produit",
        #     name="objet_ptr",
        # ),
        # migrations.RemoveField(
        #     model_name="produit",
        #     name="premiere_etape",
        # ),
        # migrations.RemoveField(
        #     model_name="quantiteressource",
        #     name="ressource",
        # ),
        # migrations.RemoveField(
        #     model_name="ressource",
        #     name="objet_ptr",
        # ),
        # migrations.RemoveField(
        #     model_name="siegesocial",
        #     name="ville",
        # ),
        # migrations.RemoveField(
        #     model_name="stock",
        #     name="ressource",
        # ),
        # migrations.RemoveField(
        #     model_name="usine",
        #     name="machines",
        # ),
        # migrations.RemoveField(
        #     model_name="usine",
        #     name="ville",
        # ),
        # migrations.RemoveField(
        #     model_name="ville",
        #     name="prix_m2",
        # ),
        migrations.AlterField(
            model_name="ville",
            name="code_postal",
            field=models.IntegerField(),
        ),
        # migrations.DeleteModel(
        #     name="Etape",
        # ),
        # migrations.DeleteModel(
        #     name="Machine",
        # ),
        # migrations.DeleteModel(
        #     name="Objet",
        # ),
        # migrations.DeleteModel(
        #     name="Produit",
        # ),
        # migrations.DeleteModel(
        #     name="QuantiteRessource",
        # ),
        # migrations.DeleteModel(
        #     name="Ressource",
        # ),
        # migrations.DeleteModel(
        #     name="SiegeSocial",
        # ),
        # migrations.DeleteModel(
        #     name="Stock",
        # ),
        # migrations.DeleteModel(
        #     name="Usine",
        # ),
    ]
