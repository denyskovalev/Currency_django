# Generated by Django 4.0.6 on 2022-08-14 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0006_alter_responselog_response_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='mail_id',
        ),
    ]