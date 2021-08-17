# Generated by Django 3.2.6 on 2021-08-17 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='post',
            name='image_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]
