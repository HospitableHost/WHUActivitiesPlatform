# Generated by Django 3.2.8 on 2021-11-22 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanage', '0005_auto_20211122_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='id',
        ),
        migrations.RemoveField(
            model_name='commenttoactivity',
            name='id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='activity',
            name='activity_id',
            field=models.CharField(max_length=40, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='activity',
            name='user_id',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='application',
            name='application_id',
            field=models.CharField(max_length=40, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='application',
            name='user_id',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='banuser',
            name='activity_id',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='banuser',
            name='banned_user_id',
            field=models.CharField(max_length=40, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='banuser',
            name='org_admin_id',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='banuser',
            name='user_id',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user_id',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='commenttoactivity',
            name='activity_id',
            field=models.CharField(max_length=40, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='commenttoactivity',
            name='comment_id',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='problem_id',
            field=models.CharField(max_length=40, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='user_id',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='participate',
            name='activity_id',
            field=models.CharField(max_length=40, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='participate',
            name='user_id',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.CharField(max_length=40, primary_key=True, serialize=False),
        ),
    ]
