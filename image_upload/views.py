from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from ipware import get_client_ip

from . import forms, models


class UUIDMixin:
    def get_object(self, queryset=None):
        instance = get_object_or_404(models.UploadedImage, uuid=self.kwargs.get("uuid"))
        return instance


class UploadImageView(LoginRequiredMixin, CreateView):
    form_class = forms.UploadImageForm
    template_name = "upload.html"

    def get_success_url(self):
        return reverse("image-detail", kwargs={"uuid": self.object.uuid})

    def get_form(self, form_class=form_class):
        ip, _ = get_client_ip(self.request)
        return form_class(ip_address=ip, **self.get_form_kwargs())


class DetailUploadImageView(UUIDMixin, DetailView):
    model = models.UploadedImage
    template_name = "detail.html"


class DeleteUploadImageView(UUIDMixin, DeleteView):
    model = models.UploadedImage
    template_name = "delete.html"

    def delete(self, request, *args, **kwargs):
        ip, _ = get_client_ip(self.request)
        instance = self.get_object()

        if not ip == instance.uploader_ip:
            raise ValidationError("You are not the owner of the image.")

        return super().delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        instance = get_object_or_404(models.UploadedImage, uuid=self.kwargs.get("uuid"))
        return instance

    def get_success_url(self):
        return reverse("image-upload")
