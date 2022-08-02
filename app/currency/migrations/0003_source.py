# Generated by Django 4.0.6 on 2022-08-02 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0002_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_name', models.CharField(max_length=64)),
                ('source_url', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]