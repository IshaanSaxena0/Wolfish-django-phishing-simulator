# Generated by Django 4.0.5 on 2022-07-17 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailer', '0012_remove_phishingdata_data_phishingdatadict_pdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipient',
            name='valid',
            field=models.BooleanField(default=True),
        ),
    ]