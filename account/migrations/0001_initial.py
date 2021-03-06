# Generated by Django 3.0.5 on 2020-04-30 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoiceno', models.IntegerField()),
                ('transtype', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('ticket', models.IntegerField()),
                ('externalno', models.CharField(max_length=200)),
                ('cctname', models.CharField(max_length=200)),
                ('location', models.CharField(blank=True, max_length=200)),
                ('sordescription', models.TextField()),
                ('qty', models.IntegerField()),
                ('rate', models.FloatField()),
                ('gst', models.FloatField()),
                ('total', models.FloatField()),
            ],
        ),
    ]
