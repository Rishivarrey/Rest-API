# Generated by Django 3.2.8 on 2021-10-28 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_auto_20211028_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingreq',
            name='advisor_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='bookingreq',
            name='user_id',
            field=models.IntegerField(null=True),
        ),
    ]