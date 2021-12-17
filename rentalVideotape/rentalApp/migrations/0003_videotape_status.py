# Generated by Django 4.0 on 2021-12-16 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rentalApp', '0002_alter_status_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='videotape',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='rentalApp.status'),
            preserve_default=False,
        ),
    ]