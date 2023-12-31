# Generated by Django 4.2.5 on 2023-10-02 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patients', '0003_remove_patient_slug'),
        ('therapists', '0002_remove_therapist_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Monster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='patients.patient')),
                ('therapist', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='therapists.therapist')),
            ],
        ),
    ]
