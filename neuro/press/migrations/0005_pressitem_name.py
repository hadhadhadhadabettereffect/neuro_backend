# Generated by Django 2.0.7 on 2018-07-16 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('press', '0004_pressitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='pressitem',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
