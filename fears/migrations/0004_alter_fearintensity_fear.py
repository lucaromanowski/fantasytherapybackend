# Generated by Django 4.2.5 on 2023-09-20 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fears', '0003_rename_modified_fearintensity_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fearintensity',
            name='fear',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fear_intensities', to='fears.fear'),
        ),
    ]
