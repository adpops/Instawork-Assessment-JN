# Generated by Django 4.0.6 on 2022-07-21 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageApp', '0003_alter_teammember_phonenum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='phoneNum',
            field=models.CharField(max_length=16),
        ),
    ]
