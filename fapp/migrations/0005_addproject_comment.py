# Generated by Django 3.1.7 on 2021-03-19 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fapp', '0004_auto_20210319_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='addproject',
            name='comment',
            field=models.CharField(max_length=100, null=True),
        ),
    ]