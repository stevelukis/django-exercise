from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from image_upload.models import UploadedImage


class UploadImageTest(TestCase):
    def test_redirect_unauthenticated_user(self):
        response = self.client.get(reverse('image-upload'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/accounts/login/?next=/')

    def test_upload_image(self):
        # create a user
        user = User.objects.create()

        # authenticate first
        self.client.force_login(user)

        image = SimpleUploadedFile(name="image.jpg",
                                   content=b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
                                           b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
                                           b'\x02\x4c\x01\x00\x3b')

        response = self.client.post(reverse('image-upload'), data={'image': image})

        self.assertEqual(UploadedImage.objects.all().count(), 1)
