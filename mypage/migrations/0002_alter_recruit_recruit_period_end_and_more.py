# Generated by Django 4.0.6 on 2022-07-22 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruit',
            name='recruit_period_end',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='recruit',
            name='recruit_period_start',
            field=models.DateField(),
        ),
    ]
