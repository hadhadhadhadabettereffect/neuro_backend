# Generated by Django 2.0.7 on 2018-07-16 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('press', '0002_auto_20180711_2046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pressitem',
            name='polymorphic_ctype',
        ),
        migrations.RemoveField(
            model_name='pressitemimage',
            name='pressitem_ptr',
        ),
        migrations.RemoveField(
            model_name='pressitemquote',
            name='pressitem_ptr',
        ),
        migrations.DeleteModel(
            name='PressItem',
        ),
        migrations.DeleteModel(
            name='PressItemImage',
        ),
        migrations.DeleteModel(
            name='PressItemQuote',
        ),
    ]
