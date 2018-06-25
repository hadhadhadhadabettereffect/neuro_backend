# Generated by Django 2.0.6 on 2018-06-25 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PressImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('link', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PressQuote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.TextField()),
                ('publication', models.CharField(blank=True, max_length=200)),
                ('author', models.CharField(blank=True, max_length=200)),
                ('link', models.URLField(blank=True)),
            ],
        ),
    ]
