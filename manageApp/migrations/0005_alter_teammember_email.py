# Generated by Django 4.0.6 on 2022-07-21 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageApp', '0004_alter_teammember_phonenum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='email',
            field=models.CharField(max_length=255),
        ),
    ]
