# Generated by Django 5.1.3 on 2024-11-29 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_place_author_alter_place_city_alter_place_photo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Bookmark',
        ),
    ]