# Generated by Django 3.2.3 on 2021-05-21 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BugReport', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bug',
            name='fieldName',
        ),
        migrations.AddField(
            model_name='bug',
            name='site_id',
            field=models.CharField(default='index.html', max_length=200),
        ),
    ]
