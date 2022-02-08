from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from files_from_user import views

urlpatterns = [
    path('', views.ImgUpload.as_view(), name="files_upload")
]

urlpatterns = format_suffix_patterns(urlpatterns)
