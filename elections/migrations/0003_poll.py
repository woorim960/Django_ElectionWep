# Generated by Django 2.2.6 on 2019-11-24 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0002_auto_20191124_1223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('area', models.CharField(max_length=15)),
            ],
        ),
    ]
