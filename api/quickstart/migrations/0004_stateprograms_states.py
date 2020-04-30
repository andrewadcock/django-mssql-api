# Generated by Django 2.2.12 on 2020-04-30 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0003_answers_questionelement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stateprograms',
            fields=[
                ('programcode', models.AutoField(db_column='ProgramCode', primary_key=True, serialize=False)),
                ('programdescription', models.CharField(blank=True, db_column='ProgramDescription', max_length=100, null=True)),
                ('startyear', models.CharField(blank=True, db_column='StartYear', max_length=4, null=True)),
                ('endyear', models.CharField(blank=True, db_column='EndYear', max_length=4, null=True)),
                ('primaryprogram', models.BooleanField(blank=True, db_column='PrimaryProgram', null=True)),
                ('medicaid', models.BooleanField(blank=True, db_column='Medicaid', null=True)),
            ],
            options={
                'db_table': 'StatePrograms',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('statecode', models.CharField(db_column='StateCode', max_length=2, primary_key=True, serialize=False)),
                ('statename', models.CharField(blank=True, db_column='StateName', max_length=50, null=True)),
            ],
            options={
                'db_table': 'States',
                'managed': False,
            },
        ),
    ]