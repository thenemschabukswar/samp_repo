# Generated by Django 4.1.3 on 2022-11-15 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0007_patient_room_alter_hosp_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hosp',
            old_name='id',
            new_name='r_id',
        ),
    ]
