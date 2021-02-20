from django.db import models
from django.contrib.auth.models import User, Group
from django.core.validators import FileExtensionValidator
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from django.utils import timezone
import uuid
import datetime


class EventLog(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    timestamp = models.DateTimeField(default = timezone.now)
    spss_file = models.FileField(upload_to ='files/', blank=True, null=True)
    excel_file = models.FileField(upload_to ='files/', blank=True, null=True)

    def __str__(self):
        return "%s" % (self.id,)
