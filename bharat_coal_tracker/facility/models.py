from django.db import models
from django.db.models import BooleanField, CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

FACILITY_TYPES = (
    ("MINE", "Mine"),
    ("WASHERY", "Washery"),
    ("RAILWAY", "Railway"),
    ("PORT", "Port"),
    ("POWER_PLANT", "Power Plant"),
    ("OTHER", "Other"),
)


class Facility(models.Model):
    id = models.AutoField(primary_key=True)
    name = CharField(_("Name of Facility"), max_length=255)
    address = CharField(max_length=200)
    type = CharField(max_length=100, choices=FACILITY_TYPES, default="OTHER")
    is_active = BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self) -> str:
        return reverse("facility:detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Facilities"
        app_label = "facility"
