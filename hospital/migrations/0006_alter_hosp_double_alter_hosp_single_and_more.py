# Generated by Django 4.1.3 on 2022-11-15 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0005_hosp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hosp',
            name='double',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='hosp',
            name='single',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='hosp',
            name='triple',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]