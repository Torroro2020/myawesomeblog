# Generated by Django 3.1.7 on 2021-04-04 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210404_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='blog_title',
            field=models.CharField(max_length=100),
        ),
    ]
