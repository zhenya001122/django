# Generated by Django 4.2.1 on 2024-04-10 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='women',
            old_name='is_publishet',
            new_name='is_published',
        ),
    ]