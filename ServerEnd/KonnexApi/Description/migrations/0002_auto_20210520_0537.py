# Generated by Django 3.2.3 on 2021-05-20 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Description', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='description',
            old_name='description',
            new_name='Description',
        ),
        migrations.RenameField(
            model_name='description',
            old_name='fieldName',
            new_name='FieldName',
        ),
    ]
