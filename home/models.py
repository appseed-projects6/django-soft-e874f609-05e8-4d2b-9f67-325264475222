# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Undefined(models.Model):

    #__Undefined_FIELDS__

    #__Undefined_FIELDS__END

    class Meta:
        verbose_name        = _("Undefined")
        verbose_name_plural = _("Undefined")


class Printer(models.Model):

    #__Printer_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)

    #__Printer_FIELDS__END

    class Meta:
        verbose_name        = _("Printer")
        verbose_name_plural = _("Printer")


class Filament(models.Model):

    #__Filament_FIELDS__
    brand = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)
    color = models.CharField(max_length=255, null=True, blank=True)
    where_bought = models.CharField(max_length=255, null=True, blank=True)

    #__Filament_FIELDS__END

    class Meta:
        verbose_name        = _("Filament")
        verbose_name_plural = _("Filament")


class Printjob(models.Model):

    #__Printjob_FIELDS__
    id = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    when_started = models.CharField(max_length=255, null=True, blank=True)
    when_finished = models.CharField(max_length=255, null=True, blank=True)

    #__Printjob_FIELDS__END

    class Meta:
        verbose_name        = _("Printjob")
        verbose_name_plural = _("Printjob")



#__MODELS__END
