# Generated by Django 5.1.4 on 2025-01-08 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mbti', '0004_mbtidescription'),
    ]

    operations = [
        migrations.AddField(
            model_name='mbtidescription',
            name='is_vague',
            field=models.BooleanField(default=False),
        ),
    ]
