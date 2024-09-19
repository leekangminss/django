# Generated by Django 5.1 on 2024-09-03 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True, unique=True, verbose_name='email')),
                ('user_id', models.CharField(blank=True, max_length=30, null=True)),
                ('thumbnail', models.CharField(blank=True, default='default_profile.jpg', max_length=256, null=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.EmailField(max_length=100, verbose_name='email')),
                ('following', models.EmailField(max_length=100, verbose_name='email')),
                ('is_live', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'follow',
                'indexes': [models.Index(fields=['follower'], name='follow_followe_227ce4_idx'), models.Index(fields=['following'], name='follow_followi_9fea95_idx')],
                'constraints': [models.UniqueConstraint(fields=('follower', 'following'), name='follower-following')],
            },
        ),
    ]
