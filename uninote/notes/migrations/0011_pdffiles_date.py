# Generated by Django 2.2.2 on 2019-07-28 19:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0010_auto_20190727_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdffiles',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]