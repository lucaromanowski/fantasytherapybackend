# Generated by Django 4.2.5 on 2023-09-26 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('therapists', '0002_remove_therapist_slug'),
        ('patients', '0003_remove_patient_slug'),
        ('followers', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PatientTherapistConnection',
            new_name='PatientTherapistRelationship',
        ),
    ]
