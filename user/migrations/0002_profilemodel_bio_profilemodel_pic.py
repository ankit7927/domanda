# Generated by Django 5.0.6 on 2024-05-31 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='bio',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='media/pics'),
        ),
    ]