# Generated by Django 2.0.2 on 2018-03-21 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20180316_0841'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='prosmotr',
            field=models.IntegerField(default=1),
        ),
    ]