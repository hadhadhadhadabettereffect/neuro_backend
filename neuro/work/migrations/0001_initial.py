# Generated by Django 2.0.6 on 2018-07-01 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work.Project')),
            ],
        ),
    ]
