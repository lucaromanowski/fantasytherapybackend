# Generated by Django 4.2.5 on 2023-10-02 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_remove_patient_slug'),
        ('therapists', '0002_remove_therapist_slug'),
        ('monsters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monster',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='monsters', to='patients.patient'),
        ),
        migrations.AlterField(
            model_name='monster',
            name='therapist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='monsters', to='therapists.therapist'),
        ),
    ]
