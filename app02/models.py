# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Publishernew(models.Model):
    pid=models.IntegerField('pod',blank=True, auto_created=True)
    name=models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Booknew(models.Model):
    title=models.CharField(max_length=64)
    pub=models.ForeignKey("Publishernew")

    def __str__(self):
        return self.title
