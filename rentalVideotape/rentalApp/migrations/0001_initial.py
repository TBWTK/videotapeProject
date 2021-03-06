# Generated by Django 4.0 on 2021-12-16 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('age', models.IntegerField(verbose_name=range(1, 200))),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Videotape',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('released', models.DateField()),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.FileField(upload_to='files/')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rentalApp.director')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rentalApp.genre')),
            ],
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('buyer_name', models.CharField(max_length=50)),
                ('buyer_surname', models.CharField(max_length=50)),
                ('buyer_email', models.EmailField(max_length=254)),
                ('buyer_phone', models.CharField(max_length=30)),
                ('videotape', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rentalApp.videotape')),
            ],
        ),
    ]
