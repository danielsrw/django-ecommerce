# Generated by Django 5.0 on 2024-01-19 19:37

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.FileField(default='category.jpg', upload_to='category', validators=[base.models.validate_svg]),
        ),
    ]
