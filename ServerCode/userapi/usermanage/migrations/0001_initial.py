# Generated by Django 3.2.8 on 2021-10-08 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('activity_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('organization_id', models.CharField(max_length=20)),
                ('activity_type', models.IntegerField()),
                ('activity_title', models.CharField(max_length=30)),
                ('publish_time', models.DateTimeField()),
                ('activity_detail', models.TextField()),
                ('parti_ddl', models.DateTimeField()),
                ('oriented_department', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('activity_id', models.IntegerField()),
                ('comment_time', models.DateTimeField()),
                ('comment_content', models.CharField(max_length=140)),
                ('user_status', models.CharField(default='普通用户', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_nickname', models.CharField(max_length=14)),
                ('user_name', models.CharField(max_length=5)),
                ('school_id', models.CharField(max_length=13)),
                ('user_auth', models.CharField(default='普通用户', max_length=5)),
                ('is_banned', models.IntegerField(default=0)),
                ('department', models.CharField(max_length=10)),
            ],
        ),
    ]