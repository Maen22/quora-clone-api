# Generated by Django 3.2.4 on 2021-06-26 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='votes',
            new_name='voters',
        ),
    ]
