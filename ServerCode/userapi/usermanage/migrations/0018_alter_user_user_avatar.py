# Generated by Django 3.2.3 on 2021-11-25 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanage', '0017_alter_activity_activity_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_avatar',
            field=models.CharField(max_length=140, null=True),
        ),
    ]
