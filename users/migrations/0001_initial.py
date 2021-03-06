# Generated by Django 2.0.5 on 2018-07-02 22:24

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ecore', '0001_initial'),
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=80, unique=True)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('mobile', models.CharField(blank=True, max_length=30)),
                ('status', models.CharField(default='pending', max_length=255)),
                ('fb_pic', models.URLField(max_length=255, null=True)),
                ('google_pic', models.URLField(max_length=255, null=True)),
                ('user_pic', models.URLField(max_length=255, null=True)),
                ('fb_verified', models.BooleanField(default=False)),
                ('google_verified', models.BooleanField(default=False)),
                ('otp', models.CharField(max_length=10, null=True)),
                ('otp_created_at', models.DateTimeField(null=True)),
                ('otp_expires_at', models.DateTimeField(null=True)),
                ('otps_sent', models.IntegerField(default=0)),
                ('otp_limit_start_time', models.DateTimeField(null=True)),
                ('otp_limit_end_time', models.DateTimeField(null=True)),
                ('user_uuid', models.UUIDField(blank=True, default=uuid.uuid4, null=True, unique=True)),
                ('verification_token', models.UUIDField(blank=True, default=uuid.uuid4, null=True, unique=True)),
                ('subscribe', models.BooleanField(default=True)),
                ('agreed_terms', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ecore.Role')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
