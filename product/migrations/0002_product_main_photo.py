# Generated by Django 4.2.17 on 2024-12-14 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='main_photo',
            field=models.URLField(blank=True, null=True),
        ),
    ]
