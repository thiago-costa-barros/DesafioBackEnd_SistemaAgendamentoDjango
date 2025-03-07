# Generated by Django 5.1.6 on 2025-02-16 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professionals', '0003_alter_healthprofessional_profession'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthprofessional',
            name='adress_number',
            field=models.CharField(blank=True, db_column='AddressNumber', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='healthprofessional',
            name='taxnumber',
            field=models.CharField(db_column='TaxNumber', default='', max_length=20, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='healthprofessional',
            name='adress_neighborhood',
            field=models.TextField(blank=True, db_column='AddressNeighborhood', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='healthprofessional',
            name='adress_street',
            field=models.TextField(blank=True, db_column='AddressStreet', max_length=255, null=True),
        ),
    ]
