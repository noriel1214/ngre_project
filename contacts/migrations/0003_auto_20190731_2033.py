# Generated by Django 2.2.3 on 2019-07-31 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20190728_1853'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='address',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='lastname',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='listing_id',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='user_id',
        ),
    ]