# Generated by Django 3.2.4 on 2021-07-19 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20210713_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='attantion',
            name='start_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='freezed',
            field=models.BooleanField(default=False),
        ),
    ]