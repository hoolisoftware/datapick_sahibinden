# Generated by Django 4.1.7 on 2023-03-15 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datapick', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='price',
            field=models.CharField(max_length=55),
        ),
    ]