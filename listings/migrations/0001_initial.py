# Generated by Django 2.2.3 on 2019-07-27 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(choices=[('AK', 'Alaska'), ('CA', 'California'), ('NJ', 'New Jersey'), ('NY', 'New York')], max_length=2)),
                ('price', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('garage', models.IntegerField()),
                ('description', models.TextField(blank=True)),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('photo_1', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('photo_2', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('photo_3', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('photo_4', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('photo_5', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('photo_6', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.Realtor')),
            ],
        ),
    ]
