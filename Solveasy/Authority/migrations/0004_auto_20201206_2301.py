# Generated by Django 3.1 on 2020-12-06 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authority', '0003_auto_20201206_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otherdetails',
            name='choice',
            field=models.CharField(choices=[('institute', 'INSTITUTE'), ('student', 'STUDENT')], default='institute', max_length=10, null=True),
        ),
    ]
