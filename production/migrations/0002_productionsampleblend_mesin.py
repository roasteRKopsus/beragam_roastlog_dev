# Generated by Django 3.0.3 on 2020-07-16 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productionsampleblend',
            name='mesin',
            field=models.CharField(choices=[('froco-15', 'froco-15'), ('froco-25', 'froco-25')], default='', max_length=50),
        ),
    ]
