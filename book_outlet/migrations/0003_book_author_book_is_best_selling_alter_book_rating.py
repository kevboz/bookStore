# Generated by Django 5.1.5 on 2025-01-22 14:00

import django.core.validators
from django.db import migrations, models



class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0002_remove_book_author_remove_book_cover_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='is_best_selling',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
