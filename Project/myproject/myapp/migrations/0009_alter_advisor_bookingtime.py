# Generated by Django 3.2.8 on 2021-10-28 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_advisor_bookingtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advisor',
            name='bookingtime',
            field=models.DateTimeField(default='9999-99-99 99:99'),
        ),
    ]
