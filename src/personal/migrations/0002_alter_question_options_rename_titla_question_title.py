# Generated by Django 4.2.6 on 2023-10-13 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("personal", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="question",
            options={
                "verbose_name": "The Question",
                "verbose_name_plural": "Peoples Questions",
            },
        ),
        migrations.RenameField(
            model_name="question",
            old_name="titla",
            new_name="title",
        ),
    ]