# Generated by Django 3.1.2 on 2020-10-11 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='password',
            field=models.CharField(max_length=500),
        ),
    ]
