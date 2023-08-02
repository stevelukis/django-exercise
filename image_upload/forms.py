from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from . import models


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = models.UploadedImage
        fields = ['image']

    def __init__(self, *args, **kwargs):
        ip_address = kwargs.pop("ip_address")

        if not ip_address:
            raise ValidationError("No IP address detected")

        self.ip_address = ip_address
        super().__init__(*args, **kwargs)

    def clean(self):
        today_count = models.UploadedImage.objects.filter(uploader_ip=self.ip_address,
                                                          upload_date=timezone.now().date()).count()
        if today_count >= models.UploadedImage.MAX_IMAGE_PER_IP_PER_DAY:
            raise ValidationError("You have exceeded the daily upload limit. Please try again tomorrow.")
        return super().clean()

    def save(self, commit=True):
        self.instance.uploader_ip = self.ip_address
        return super().save(commit)
