# Generated by Django 3.1.6 on 2021-02-11 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_auto_20210211_1821"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="magic_link",
        ),
    ]
