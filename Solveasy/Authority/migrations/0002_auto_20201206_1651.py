# Generated by Django 3.1.2 on 2020-12-06 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authority', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodavbl',
            name='edible',
        ),
        migrations.RemoveField(
            model_name='foodavbl',
            name='measurement',
        ),
        migrations.RemoveField(
            model_name='foodavbl',
            name='pickup_address',
        ),
        migrations.RemoveField(
            model_name='foodavbl',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='foodavbl',
            name='typee',
        ),
        migrations.RemoveField(
            model_name='history',
            name='edible',
        ),
        migrations.RemoveField(
            model_name='history',
            name='measurement',
        ),
        migrations.RemoveField(
            model_name='history',
            name='pickup_address',
        ),
        migrations.RemoveField(
            model_name='history',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='history',
            name='typee',
        ),
        migrations.AddField(
            model_name='foodavbl',
            name='problem_title',
            field=models.CharField(default='enter', max_length=100),
        ),
        migrations.AlterField(
            model_name='foodavbl',
            name='Other_Specifics',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='foodavbl',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='Authority/images'),
        ),
        migrations.DeleteModel(
            name='Measurement',
        ),
        migrations.DeleteModel(
            name='TypeOf',
        ),
    ]