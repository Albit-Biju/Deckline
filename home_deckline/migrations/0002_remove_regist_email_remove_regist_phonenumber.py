# Generated by Django 5.0.6 on 2024-06-06 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_deckline', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regist',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='regist',
            name='phoneNumber',
        ),
    ]
