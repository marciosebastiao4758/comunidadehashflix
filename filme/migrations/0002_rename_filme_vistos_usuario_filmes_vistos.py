# Generated by Django 4.2.4 on 2023-08-09 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("filme", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="usuario",
            old_name="filme_vistos",
            new_name="filmes_vistos",
        ),
    ]
