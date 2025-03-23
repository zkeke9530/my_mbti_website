# Generated by Django 5.1.4 on 2025-01-18 17:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mbti', '0007_alter_mbtisentence_mbti_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='MBTIDescriptionModified',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mbti_type', models.CharField(max_length=4, unique=True)),
                ('description', models.TextField()),
                ('image', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameModel(
            old_name='MBTIDescription',
            new_name='MBTIDescriptionTrue',
        ),
        migrations.RenameModel(
            old_name='MBTISentence',
            new_name='MBTISentenceTrue',
        ),
        migrations.CreateModel(
            name='MBTISentenceModified',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentence', models.TextField()),
                ('is_vague', models.BooleanField(default=False)),
                ('mbti_description', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mbti.mbtidescriptionmodified')),
            ],
        ),
    ]
