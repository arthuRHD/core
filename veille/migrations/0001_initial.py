# Generated by Django 3.0.3 on 2020-03-05 08:23

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('desc', models.TextField(default=None)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('thumbnail', models.ImageField(upload_to='D:\\projects\\web\\django-portfolio\\src\\media\\upload/')),
                ('date', models.DateField(auto_now_add=True)),
                ('source', models.ManyToManyField(to='veille.Source')),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veille.Theme')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
