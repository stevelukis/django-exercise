import uuid

from django.db import models


class UploadedImage(models.Model):
    MAX_IMAGE_PER_IP_PER_DAY = 10

    image = models.ImageField(upload_to='uploads/')
    upload_date = models.DateField(auto_now_add=True)
    uploader_ip = models.GenericIPAddressField()
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
