# Generated by Django 3.1.4 on 2021-01-02 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='target',
            field=models.IntegerField(max_length=10),
        ),
    ]
