# Generated by Django 2.0.4 on 2018-04-15 19:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost_per_km', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('price', models.DecimalField(decimal_places=3, default='0', max_digits=20)),
                ('registration_plate', models.CharField(default='', max_length=200)),
                ('vehicle_status', models.CharField(choices=[('B', 'Booked'), ('NB', 'Not Booked')], default='NB', max_length=2)),
                ('insurance_status', models.CharField(choices=[('U', 'Updated'), ('NU', 'Not Updated')], default='NU', max_length=2)),
                ('no_of_km_travelled', models.DecimalField(decimal_places=0, default=0, max_digits=20)),
                ('fuel_type', models.CharField(choices=[('P', 'Petrol'), ('D', 'Diesel')], default='P', max_length=1)),
                ('mileage', models.DecimalField(decimal_places=0, default=0, max_digits=20)),
                ('vehicle_type', models.CharField(choices=[('P', 'Passenger'), ('T', 'Truck'), ('C', 'Construction')], default='P', max_length=1)),
                ('image', models.ImageField(blank=True, default='default.png', upload_to='vehicle_image')),
                ('owner', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
