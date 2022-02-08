from django.db import models
from random import randrange
from django.contrib.auth import get_user_model
import os
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from django.utils.translation import ugettext_lazy as _
"""
Creats Custom Path inMedia Folder But If User Is Not  Authenticated
Usese a default value -1 for anonymous user
"""

def custom_dir(instance, filename):
    now= timezone.now()
    base, extension = os.path.splitext(filename)
    extension = extension.lower()
    return f"files_to_process/{instance.user if instance.is_auth else 'anon'}_{instance.id}/{now:%Y-%m-%d}/file_{instance.id}{extension}"

# Create your models here.
class Image_to_eval(models.Model):
    file = models.FileField(upload_to=custom_dir, null=False, blank=False, verbose_name=_("Upload"), validators=[FileExtensionValidator(['JPEG', 'PNG', 'GIF', 'JPG', 'TIFF', 'EPS', 'RAW', 'ICO'], "Please upload an image with one of \
    the following extensions 'JPEG', 'PNG', 'GIF', 'JPG', 'TIFF', 'EPS', 'RAW', 'ICO'")], default='settings.MEDIA_ROOT/default/home')
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, help_text=_("User That uploaded file."), null=True, blank=True, verbose_name=_("User"), default=None)
    date_up = models.DateTimeField(_("when was uploaded"), default=timezone.now, editable=False)
    is_auth = models.BooleanField(_("User Is Authenticated"), default=False, help_text=_("True if the user is part of our community i.e registered."))
    hey = "Curva"

    class Meta:
        verbose_name = "File"
        verbose_name_plural = "Files"

