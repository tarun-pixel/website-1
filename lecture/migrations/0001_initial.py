# Generated by Django 2.0.2 on 2018-02-19 20:25

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
            name='Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Lecture Name')),
                ('classroom', models.CharField(blank=True, max_length=255, null=True, verbose_name='Classroom')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Start Date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='End Date')),
                ('is_registration_open', models.BooleanField(default=False, verbose_name='Open for Registration')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('lecturer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lectures', to=settings.AUTH_USER_MODEL, verbose_name='Lecturer')),
            ],
            options={
                'verbose_name': 'Lecture',
                'verbose_name_plural': 'Lectures',
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='LectureSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField(verbose_name='Start Time')),
                ('end_time', models.TimeField(verbose_name='End Time')),
                ('day_of_week', models.IntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')], default=1)),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='lecture.Lecture', verbose_name='Lecture')),
            ],
            options={
                'verbose_name': 'Lecture Schedule',
                'verbose_name_plural': 'Lecture Schedules',
                'ordering': ('day_of_week', 'start_time'),
            },
        ),
    ]
