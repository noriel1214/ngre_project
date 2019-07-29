# Generated by Django 2.2.3 on 2019-07-27 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_listing_is_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='bathrooms',
            field=models.FloatField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='lotsize',
            field=models.FloatField(default=2.2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='sqft',
            field=models.IntegerField(default=3000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listing',
            name='garage',
            field=models.IntegerField(default=0),
        ),
    ]
