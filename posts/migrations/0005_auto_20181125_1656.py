# Generated by Django 2.1.3 on 2018-11-25 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20181125_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_published',
            field=models.DateTimeField(verbose_name='%m/%d/%Y'),
        ),
    ]
