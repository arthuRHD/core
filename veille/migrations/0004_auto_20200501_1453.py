# Generated by Django 3.0.3 on 2020-05-01 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('veille', '0003_auto_20200306_1123'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['date']},
        ),
    ]
