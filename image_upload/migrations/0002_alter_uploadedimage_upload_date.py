# Generated by Django 4.2.3 on 2023-07-30 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_upload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedimage',
            name='upload_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]