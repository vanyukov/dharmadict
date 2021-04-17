import logging
import datetime
import json
from datetime import datetime
from import_export import resources

from django.db import models
from django.db import migrations, models

from core.models import (CustomUser)

class Term(models.Model):
    wylie = models.CharField(max_length = 216)
    sanscrit = models.CharField(max_length = 216)
    tibetian = models.CharField(max_length = 216)
    sa2ru = models.CharField(max_length = 216)
    sa2en = models.CharField(max_length = 216)


class Transtation(models.Model):
    term = models.ForeignKey(Term, on_delete=models.CASCADE, related_name='term')
