# Generated by Django 4.0.6 on 2022-07-27 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0006_recruit_recruit_hashtag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruit',
            name='recruit_hashtag',
            field=models.ManyToManyField(blank=True, to='mypage.hashtag'),
        ),
    ]