# Generated by Django 4.2.5 on 2023-10-02 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monsters', '0002_alter_monster_patient_alter_monster_therapist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monster',
            name='therapist',
        ),
    ]
