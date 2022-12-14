# Generated by Django 4.1.3 on 2022-11-14 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='id',
        ),
        migrations.AddField(
            model_name='patient',
            name='allergies',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='patient',
            name='disease',
            field=models.CharField(default='fever', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='hospital',
            field=models.CharField(default='tortis', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='p_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='remarks',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='patient',
            name='status',
            field=models.CharField(choices=[('Primary', 'Primary Checkup'), ('Admitted', 'Admitted'), ('Discharged', 'Discharged')], default='Primary', max_length=20),
        ),
    ]
