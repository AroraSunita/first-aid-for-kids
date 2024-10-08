# Generated by Django 4.2.14 on 2024-08-10 22:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_course_image_alter_booking_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='booking',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.CharField(default='09:00 - 10:00', max_length=20),
        ),
        migrations.AlterField(
            model_name='contact',
            name='comment',
            field=models.TextField(max_length=20000),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
