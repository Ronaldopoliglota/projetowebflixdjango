# Generated by Django 4.2.1 on 2023-06-07 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filme', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='filmes_visto',
            new_name='filmes_vistos',
        ),
    ]
