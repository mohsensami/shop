# Generated by Django 4.1.3 on 2022-11-21 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.CharField(max_length=300),
        ),
    ]