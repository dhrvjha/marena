# Generated by Django 3.0.3 on 2020-03-22 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200322_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='author',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='comment',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]