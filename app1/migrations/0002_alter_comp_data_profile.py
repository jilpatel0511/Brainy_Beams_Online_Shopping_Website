# Generated by Django 3.2.3 on 2021-06-05 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comp_data',
            name='profile',
            field=models.ImageField(blank=True, default='', max_length='300', null=True, upload_to='Comp_profile/'),
        ),
    ]
