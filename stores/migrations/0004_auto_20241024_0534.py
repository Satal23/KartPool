# Generated by Django 3.0.6 on 2024-10-24 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0003_auto_20241024_0450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='lat',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='lon',
            field=models.FloatField(null=True),
        ),
    ]
