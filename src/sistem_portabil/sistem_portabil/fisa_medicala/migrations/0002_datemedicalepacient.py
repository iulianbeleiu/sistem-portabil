# Generated by Django 2.2.12 on 2020-06-01 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pacient', '0006_auto_20200527_1924'),
        ('fisa_medicala', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DateMedicalePacient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_medicale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacient.DateMedicale')),
                ('pacient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacient.Pacient')),
            ],
        ),
    ]