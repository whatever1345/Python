# Generated by Django 2.0.2 on 2018-03-11 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0015_auto_20180305_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='message',
            field=models.TextField(default='message'),
        ),
    ]
