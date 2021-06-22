# Generated by Django 3.2.4 on 2021-06-22 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attantion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_num', models.IntegerField(default=1)),
            ],
        ),
        migrations.AlterField(
            model_name='group',
            name='course',
            field=models.ForeignKey(default=14, on_delete=django.db.models.deletion.SET_DEFAULT, to='api.course'),
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(null=True)),
                ('time', models.TimeField(null=True)),
                ('attantion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.attantion')),
            ],
        ),
        migrations.AddField(
            model_name='attantion',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.group'),
        ),
    ]