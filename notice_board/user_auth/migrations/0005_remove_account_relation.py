# Generated by Django 4.0.4 on 2022-05-12 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0004_account_relation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='relation',
        ),
    ]
