# Generated by Django 5.1.4 on 2024-12-24 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mbti', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('dimension', models.CharField(choices=[('EI', '外向(E) / 内向(I)'), ('SN', '实感(S) / 直觉(N)'), ('TF', '思考(T) / 情感(F)'), ('JP', '判断(J) / 感知(P)')], max_length=2)),
                ('option_1', models.CharField(default='strongly disagree', max_length=100)),
                ('option_2', models.CharField(default='disagree', max_length=100)),
                ('option_3', models.CharField(default='neutral', max_length=100)),
                ('option_4', models.CharField(default='agree', max_length=100)),
                ('option_5', models.CharField(default='strongly agree', max_length=100)),
            ],
        ),
    ]
