# Generated by Django 3.2.3 on 2021-05-20 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fieldName', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
            ],
        ),
    ]