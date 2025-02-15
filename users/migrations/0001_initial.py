# Generated by Django 5.1.6 on 2025-02-15 13:03

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(db_column='UserId', primary_key=True, serialize=False)),
                ('username', models.CharField(db_column='Username', max_length=150, unique=True)),
                ('email', models.EmailField(db_column='Email', max_length=254, unique=True)),
                ('first_name', models.CharField(db_column='FirstName', max_length=30)),
                ('last_name', models.CharField(db_column='LastName', max_length=150)),
                ('date_joined', models.DateTimeField(auto_now_add=True, db_column='DateJoined')),
                ('is_active', models.BooleanField(db_column='IsActive', default=True)),
                ('is_staff', models.BooleanField(db_column='IsStaff', default=False)),
                ('is_superuser', models.BooleanField(db_column='IsSuperUser', default=False)),
                ('password', models.CharField(db_column='Password', max_length=128)),
                ('last_login', models.DateTimeField(blank=True, db_column='LastLogin', null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'User',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
