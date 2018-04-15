# Generated by Django 2.0.4 on 2018-04-13 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('nationalId', models.CharField(max_length=13)),
                ('address', models.CharField(max_length=1000)),
                ('email', models.CharField(max_length=300)),
                ('phoneNumber', models.CharField(max_length=10)),
                ('licenseCategory', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('B', 'booked'), ('NB', 'not booked')], default='NB', max_length=2)),
            ],
        ),
    ]