# Generated by Django 3.2.3 on 2021-11-25 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanage', '0015_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_avatar',
            field=models.CharField(default='https://img2.baidu.com/it/u=844091630,1508654762&fm=26&fmt=auto', max_length=140),
        ),
    ]
