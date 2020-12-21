from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class RegularPlan(models.Model):
    cycle_choices = (
        ("Daily", "Daily"),
        ("Weekly", "Weekly")
    )

    type_choices = (
        ("Bi-Time", "Bi-Time"),
        ("Tri-Time", "Tri-Time"),
        ("Simple", "Simple")
    )

    unit_choices = (
        ("kWh", "kWh"),
        ("min", "min")
    )

    name = models.CharField(verbose_name="Name_of_the_Plan", max_length=300)
    tar_included = models.BooleanField()
    subscription = models.FloatField(verbose_name="Monthly Subscription")
    cycle = models.CharField(verbose_name="Cycle", max_length=10, choices=cycle_choices)
    type = models.CharField(verbose_name="Type", max_length=10, choices=type_choices)
    offer_iva = models.BooleanField()
    off_peak_price = models.FloatField(verbose_name="Off Peak Price")
    peak_price = models.FloatField(verbose_name="Peak Price")
    unit = models.CharField(verbose_name="Unit", max_length=3, choices=unit_choices)
    valid = models.BooleanField(verbose_name="Valid Plan")
    publish = models.BooleanField(verbose_name="Publish")
    vat = models.IntegerField(
        verbose_name="Vat", 
        validators=[MaxValueValidator(100), 
        MinValueValidator(1)]
    )
    owner = models.ForeignKey(
        User, null=True, 
        blank=True, 
        on_delete=models.CASCADE,
        related_name='owner',
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="Regular Plan"
        verbose_name_plural="Regular Plans"
        ordering=['name']