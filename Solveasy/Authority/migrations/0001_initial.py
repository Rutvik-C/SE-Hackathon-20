# Generated by Django 3.1.2 on 2020-12-06 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='enter', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='otherDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(blank=True, max_length=250)),
                ('phonenumber', models.IntegerField(default=9898944123)),
                ('image', models.ImageField(upload_to='Authority/images')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Authority.cities')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='details', related_query_name='details', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_title', models.CharField(default='enter', max_length=100)),
                ('problem_desc', models.TextField(max_length=100)),
                ('images', models.ImageField(blank=True, null=True, upload_to='Authority/images')),
                ('city', models.CharField(default='enter', max_length=100)),
                ('created_on', models.DateTimeField(null=True)),
                ('otherDetails', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Authority.otherdetails')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='foodss', related_query_name='foodss', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Belongs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_authority', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=False)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='belong', related_query_name='belong', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
