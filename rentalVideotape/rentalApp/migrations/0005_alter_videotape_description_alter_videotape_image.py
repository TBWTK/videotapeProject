# Generated by Django 4.0 on 2021-12-16 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentalApp', '0004_alter_videotape_description_alter_videotape_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videotape',
            name='description',
            field=models.FileField(upload_to='files/'),
        ),
        migrations.AlterField(
            model_name='videotape',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]