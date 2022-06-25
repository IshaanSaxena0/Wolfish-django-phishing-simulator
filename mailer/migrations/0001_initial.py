# Generated by Django 4.0.5 on 2022-06-24 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_email', models.CharField(blank=True, max_length=255, null=True)),
                ('sender_name', models.CharField(blank=True, max_length=255, null=True)),
                ('reply_to_email', models.CharField(blank=True, max_length=255, null=True)),
                ('reply_to_name', models.CharField(blank=True, max_length=255, null=True)),
                ('subject', models.CharField(blank=True, max_length=255, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('email_list', models.TextField(blank=True, null=True)),
            ],
        ),
    ]