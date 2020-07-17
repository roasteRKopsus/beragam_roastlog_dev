# Generated by Django 3.0.3 on 2020-07-16 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roaster',
            name='density',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=19),
        ),
        migrations.AlterField(
            model_name='roaster',
            name='moisture_content',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=19),
        ),
    ]
