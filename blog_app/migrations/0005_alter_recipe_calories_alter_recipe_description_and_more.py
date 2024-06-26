# Generated by Django 4.2.6 on 2023-10-28 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0004_remove_recipe_author_id_recipe_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='calories',
            field=models.IntegerField(blank=True, verbose_name='ККал'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(verbose_name='Описание*'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='steps_cook',
            field=models.TextField(blank=True, verbose_name='Шаги'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='time_cook',
            field=models.IntegerField(verbose_name='Готовка в мин*'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Заголовок*'),
        ),
    ]
