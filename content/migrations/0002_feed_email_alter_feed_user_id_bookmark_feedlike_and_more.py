# Generated by Django 5.1 on 2024-09-03 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='feed',
            name='user_id',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, verbose_name='email')),
                ('feed_id', models.IntegerField()),
                ('is_bookmarked', models.BooleanField(default=True)),
            ],
            options={
                'indexes': [models.Index(fields=['email'], name='content_boo_email_03c3c8_idx')],
            },
        ),
        migrations.CreateModel(
            name='FeedLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed_id', models.IntegerField()),
                ('email', models.CharField(blank=True, max_length=30, null=True)),
                ('is_like', models.BooleanField(default=False)),
            ],
            options={
                'indexes': [models.Index(fields=['feed_id'], name='content_fee_feed_id_1c82cf_idx'), models.Index(fields=['email'], name='content_fee_email_3901d6_idx')],
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed_id', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.CharField(blank=True, max_length=30, null=True)),
                ('content', models.TextField()),
                ('email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='email')),
            ],
            options={
                'indexes': [models.Index(fields=['feed_id'], name='content_rep_feed_id_49ae3d_idx')],
            },
        ),
    ]
