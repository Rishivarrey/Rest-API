# Generated by Django 3.2.8 on 2021-10-28 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_myapp_advisor'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=70)),
                ('password', models.CharField(default='', max_length=70)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
