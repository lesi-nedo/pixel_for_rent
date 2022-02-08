from rest_framework import serializers
from .models import Image_to_eval

class ImageSerial(serializers.ModelSerializer):

    class Meta:
        model= Image_to_eval
        fields = '__all__'
