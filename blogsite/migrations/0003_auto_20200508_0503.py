# Generated by Django 3.0.6 on 2020-05-08 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogsite', '0002_remove_post_main_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(upload_to='static/blog/uploads/'),
        ),
    ]
