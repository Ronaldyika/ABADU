# Generated by Django 4.2.1 on 2023-07-10 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ABADUAPP', '0003_rename_blog_blogpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]
