# Generated by Django 4.2.15 on 2025-04-05 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=16)),
                ('name', models.CharField(max_length=32)),
                ('telegram_id', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=32)),
                ('role', models.CharField(max_length=16)),
                ('avatar', models.ImageField(null=True, upload_to='')),
            ],
        ),
    ]
