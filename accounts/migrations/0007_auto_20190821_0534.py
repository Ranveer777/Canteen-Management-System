# Generated by Django 2.2.2 on 2019-08-21 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_profile_idcardno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='balance',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=100),
        ),
    ]