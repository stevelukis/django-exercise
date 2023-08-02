from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path("", views.UploadImageView.as_view(), name="image-upload"),
    path("image/<uuid>/", views.DetailUploadImageView.as_view(), name="image-detail"),
    path("image/<uuid>/delete/", views.DeleteUploadImageView.as_view(), name="image-delete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
