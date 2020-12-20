# Generated by Django 3.1.4 on 2020-12-19 04:05

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RegularPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Name_of_the_Plan')),
                ('tar_included', models.BooleanField()),
                ('subscription', models.FloatField(verbose_name='Monthly Subscription')),
                ('cycle', models.CharField(choices=[('D', 'Daily'), ('W', 'Weekly')], max_length=1, verbose_name='Cycle')),
                ('type', models.CharField(choices=[('Bi-Time', 'Bi-Time'), ('Tri-Time', 'Tri-Time'), ('Simple', 'Simple')], max_length=10, verbose_name='Type')),
                ('offer_iva', models.BooleanField()),
                ('off_peak_price', models.FloatField(verbose_name='Off Peak Price')),
                ('peak_price', models.FloatField(verbose_name='Peak Price')),
                ('unit', models.CharField(choices=[('kWh', 'kWh'), ('min', 'min')], max_length=3, verbose_name='Unit')),
                ('valid', models.BooleanField(verbose_name='Valid Plan')),
                ('publish', models.BooleanField(verbose_name='Publish')),
                ('vat', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='Vat')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Regular Plan',
                'verbose_name_plural': 'Regular Plans',
                'ordering': ['name'],
            },
        ),
    ]