# Generated by Django 5.0.9 on 2024-11-04 19:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0072_entry_search_model"),
    ]

    operations = [
        migrations.DeleteModel(
            name="UserSearchModelConfig",
        ),
    ]
