# Generated by Django 4.2 on 2023-06-01 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_remove_boost_power_alter_core_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='boost',
            name='power',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='boost',
            name='lvl',
            field=models.IntegerField(default=0),
        ),
    ]
