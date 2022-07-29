# Generated by Django 4.0.5 on 2022-07-26 02:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mailer', '0014_phishingdatadict_agent_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phishingdatadict',
            name='agent_data',
        ),
        migrations.CreateModel(
            name='AgentData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.TextField(blank=True, null=True)),
                ('pdata', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mailer.phishingdata')),
            ],
        ),
    ]