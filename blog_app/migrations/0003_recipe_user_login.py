# Generated by Django 4.2.6 on 2023-10-28 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_comment_user_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='user_login',
            field=models.CharField(default='rootRecipe', max_length=200),
        ),
    ]
