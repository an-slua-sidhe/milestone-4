# Generated by Django 3.1 on 2020-08-28 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all_antiquities', '0004_auto_20200826_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antiquity',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]
