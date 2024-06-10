# Generated by Django 5.0.6 on 2024-06-10 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0015_editrecipesmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddDetailModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('text', models.TextField(verbose_name='Описание')),
            ],
        ),
        migrations.DeleteModel(
            name='Detail',
        ),
    ]
