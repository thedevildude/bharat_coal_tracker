from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from bharat_coal_tracker.facility.models import Facility


class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = CharField(_("Name of Role"), max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Roles"


class User(AbstractUser):
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE, null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)

    def get_absolute_url(self) -> str:
        return reverse("users:detail", kwargs={"username": self.username})
