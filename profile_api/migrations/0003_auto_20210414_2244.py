# Generated by Django 2.2 on 2021-04-14 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_api', '0002_profilefeeditem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilefeeditem',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
