# Generated by Django 3.1.2 on 2020-12-06 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0003_auto_20201206_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem_selected',
            name='problem_title',
            field=models.CharField(default='enter', max_length=100),
        ),
    ]
