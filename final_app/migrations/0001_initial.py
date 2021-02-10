# Generated by Django 3.1.5 on 2021-01-31 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='images')),
                ('date_upload', models.DateTimeField(auto_now_add=True)),
                ('desc', models.TextField()),
            ],
        ),
    ]
