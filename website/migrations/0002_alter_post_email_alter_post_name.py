# Generated by Django 4.2.1 on 2023-05-29 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="email",
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name="post",
            name="name",
            field=models.TextField(),
        ),
    ]