# Generated by Django 4.1.6 on 2023-02-21 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_user_citizenship_id_number_user_citizenship_image_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="phone_number",
            field=models.CharField(default="", max_length=14),
        ),
    ]