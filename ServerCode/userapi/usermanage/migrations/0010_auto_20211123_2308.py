# Generated by Django 3.2.8 on 2021-11-23 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanage', '0009_participate_parti_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('admin_id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=13)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.RenameField(
            model_name='banuser',
            old_name='comment_time',
            new_name='banned_time',
        ),
    ]
