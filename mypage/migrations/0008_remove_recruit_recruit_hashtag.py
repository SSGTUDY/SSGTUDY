# Generated by Django 4.0.6 on 2022-07-27 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0007_alter_recruit_recruit_hashtag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recruit',
            name='recruit_hashtag',
        ),
    ]
