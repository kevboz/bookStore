# Generated by Django 5.1.5 on 2025-01-25 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0003_book_author_book_is_best_selling_alter_book_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
