# Generated by Django 5.1.4 on 2025-01-08 13:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mbti', '0005_mbtidescription_is_vague'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mbtidescription',
            name='is_vague',
        ),
        migrations.CreateModel(
            name='MBTISentence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentence', models.TextField()),
                ('is_vague', models.BooleanField(default=False)),
                ('mbti_description', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sentences', to='mbti.mbtidescription')),
            ],
        ),
    ]
