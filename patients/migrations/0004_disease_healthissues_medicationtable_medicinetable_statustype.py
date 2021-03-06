# Generated by Django 2.2.12 on 2020-05-23 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_medicalcamp1_staffcount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('issue', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('risk_type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='StatusType',
            fields=[
                ('status', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='MedicineTable',
            fields=[
                ('Medicine', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.Disease')),
            ],
        ),
        migrations.CreateModel(
            name='MedicationTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.MedicineTable')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.People')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.StatusType')),
            ],
        ),
        migrations.CreateModel(
            name='HealthIssues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.Disease')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.People')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.StatusType')),
            ],
        ),
    ]
