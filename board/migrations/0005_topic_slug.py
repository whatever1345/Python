# Generated by Django 2.0.2 on 2018-03-01 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_auto_20180227_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='slug',
            field=models.SlugField(default='Else', unique=True),
        ),
    ]
