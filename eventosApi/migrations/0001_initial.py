# Generated by Django 3.1 on 2020-08-18 02:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authentication',
            fields=[
                ('username', models.CharField(max_length=200)),
                ('token', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=200)),
                ('event_category', models.CharField(max_length=200)),
                ('event_place', models.CharField(max_length=200)),
                ('event_address', models.CharField(max_length=200)),
                ('event_initial_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('event_final_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('event_type', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventosApi.user')),
            ],
        ),
    ]