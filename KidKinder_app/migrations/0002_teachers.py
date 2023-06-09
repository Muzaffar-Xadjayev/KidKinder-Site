# Generated by Django 4.1.7 on 2023-03-13 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KidKinder_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='teachers_image/')),
                ('name', models.CharField(max_length=50)),
                ('kasb', models.CharField(max_length=100)),
                ('twitter', models.CharField(blank=True, max_length=200, null=True)),
                ('facebook', models.CharField(blank=True, max_length=200, null=True)),
                ('instagram', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
