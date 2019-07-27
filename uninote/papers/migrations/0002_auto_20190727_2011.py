# Generated by Django 2.2.2 on 2019-07-27 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdffiles',
            name='files',
            field=models.FileField(default=1, upload_to='notes/myfiles'),
        ),
        migrations.AlterField(
            model_name='pdffiles',
            name='term',
            field=models.CharField(choices=[('minor1', 'minor1'), ('minor2', 'minor2'), ('major', 'major')], default=1, max_length=20),
        ),
        migrations.DeleteModel(
            name='Papers',
        ),
    ]
