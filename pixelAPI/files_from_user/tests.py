from rest_framework.test import APIClient, APITestCase
from io import BytesIO
from PIL import Image
from rest_framework import status
from django.core.files import File
from django.urls import reverse

def get_image_file(name='test.png', ext='png', size=(80, 80), color=(256, 0, 0)):
    file_obj = BytesIO()
    image = Image.new("RGBA", size=size, color=color)
    image.save(file_obj, ext)
    file_obj.seek(0)
    return File(file_obj, name=name)

class TestUpload (APITestCase):

    def test_upload(self):
        img = get_image_file()
        client = APIClient()
        url = reverse('files_upload')
        response = client.post(url, {'file': img, 'to_commit': True})
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)

# Create your tests here.

