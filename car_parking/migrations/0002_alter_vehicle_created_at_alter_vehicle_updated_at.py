# Generated by Django 4.0 on 2021-12-14 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_parking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='Updated at'),
        ),
    ]
