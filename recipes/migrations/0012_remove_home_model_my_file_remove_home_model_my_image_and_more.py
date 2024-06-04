# Generated by Django 5.0.6 on 2024-06-01 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0011_detail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home_model',
            name='my_file',
        ),
        migrations.RemoveField(
            model_name='home_model',
            name='my_image',
        ),
        migrations.AddField(
            model_name='home_model',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='home_model',
            name='title',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
