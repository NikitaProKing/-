# Generated by Django 5.0.6 on 2024-05-27 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0009_commentmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentmodel',
            old_name='content',
            new_name='text',
        ),
    ]
