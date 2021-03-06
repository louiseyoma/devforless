# Generated by Django 2.0 on 2018-01-13 12:26

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('desired_skills', models.TextField()),
                ('job_description', models.TextField()),
                ('time_of_post_creation', models.DateTimeField(default=django.utils.timezone.now)),
                ('employer', models.ForeignKey(on_delete='on_delete', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
