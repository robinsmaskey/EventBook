# Generated by Django 4.2.1 on 2023-09-26 10:22

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
            name='event_catagorey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('description', models.TextField()),
                ('city', models.TextField(default='', max_length=200)),
                ('state', models.TextField(default='', max_length=200)),
                ('date', models.DateField()),
                ('educational_leave', models.BooleanField(default=False)),
                ('max_participants', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('event_type', models.CharField(choices=[('in_person', 'In-Person'), ('online', 'Online')], default='in_person', max_length=20)),
                ('orginzer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orgnizer', to=settings.AUTH_USER_MODEL)),
                ('participants', models.ManyToManyField(blank=True, default=None, to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(to='main.tag')),
            ],
        ),
    ]
