# Generated by Django 4.1.7 on 2023-03-13 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KidKinder_app', '0003_parents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parents',
            name='picture',
            field=models.ImageField(upload_to='parents_image/'),
        ),
    ]