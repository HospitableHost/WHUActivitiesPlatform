# Generated by Django 3.2.8 on 2021-11-24 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermanage', '0011_auto_20211124_1813'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reply',
            old_name='comment_id',
            new_name='from_comment_id',
        ),
        migrations.RenameField(
            model_name='reply',
            old_name='to_id',
            new_name='to_comment_id',
        ),
    ]