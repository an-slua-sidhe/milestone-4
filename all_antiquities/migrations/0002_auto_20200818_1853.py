# Generated by Django 3.1 on 2020-08-18 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('all_antiquities', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='antiquity',
            options={'verbose_name_plural': 'Antiquities'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
