# Generated by Django 2.0.5 on 2018-06-23 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.AddField(
            model_name='user',
            name='fb_pic',
            field=models.URLField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='fb_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='google_pic',
            field=models.URLField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='google_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='otp',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='otp_created_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='otp_expires_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='otp_limit_end_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='otp_limit_start_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='otps_sent',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='user_pic',
            field=models.URLField(max_length=255, null=True),
        ),
    ]