# Generated by Django 5.0.6 on 2024-06-19 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0002_response'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]