# Generated by Django 3.0.1 on 2019-12-27 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191227_0237'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='content_detail',
            field=models.CharField(max_length=140, null=True),
        ),
    ]
