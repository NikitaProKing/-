# Generated by Django 5.0.6 on 2024-06-10 11:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0014_remove_detail_imge_detail_photo_detail_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='EditRecipesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.add_a_recipe_model')),
            ],
        ),
    ]