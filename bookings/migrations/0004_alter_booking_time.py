# Generated by Django 4.2.14 on 2024-08-10 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_alter_booking_date_alter_booking_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.CharField(default='09:00 - 10:00', max_length=20),
        ),
    ]
