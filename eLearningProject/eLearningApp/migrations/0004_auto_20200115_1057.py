# Generated by Django 3.0.2 on 2020-01-15 10:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('eLearningApp', '0003_auto_20200115_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 15, 10, 57, 23, 876157, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='course',
            name='info',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='overview',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='course',
            name='thumbnail',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='course',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 15, 10, 57, 23, 876186, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='file',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 15, 10, 57, 23, 879006, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='file',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 15, 10, 57, 23, 879029, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='image',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 15, 10, 57, 23, 879006, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='image',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 15, 10, 57, 23, 879029, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='relatedcourse',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 15, 10, 57, 23, 877073, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='text',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 15, 10, 57, 23, 879006, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='text',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 15, 10, 57, 23, 879029, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='video',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 15, 10, 57, 23, 879006, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='video',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 15, 10, 57, 23, 879029, tzinfo=utc)),
        ),
    ]
