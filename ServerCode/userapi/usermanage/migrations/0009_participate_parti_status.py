# Generated by Django 3.2.8 on 2021-11-23 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanage', '0008_auto_20211123_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='participate',
            name='parti_status',
            field=models.IntegerField(default=0),
        ),
    ]
