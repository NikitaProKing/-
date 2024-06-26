# Generated by Django 5.0.6 on 2024-05-22 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_add_a_recipe_model'),
    ]

    operations = [
        migrations.DeleteModel(
            name='News',
        ),
        migrations.AlterField(
            model_name='add_a_recipe_model',
            name='author',
            field=models.CharField(max_length=50, verbose_name='Автор блюда'),
        ),
        migrations.AlterField(
            model_name='add_a_recipe_model',
            name='content',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='add_a_recipe_model',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='add_a_recipe_model',
            name='img',
            field=models.ImageField(upload_to='', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='add_a_recipe_model',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
    ]
