# Generated by Django 4.2 on 2023-04-26 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buzzlab_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='is_trusty',
            new_name='verified',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='favorite_labs',
            field=models.ManyToManyField(blank=True, to='buzzlab_app.lab'),
        ),
    ]
