# Generated by Django 5.0.6 on 2024-06-11 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_user_internal_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='num_applications',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
