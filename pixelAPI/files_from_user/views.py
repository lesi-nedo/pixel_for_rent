from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serial import ImageSerial
import os

ALLOWED_TYPES = {'JPEG':1 , 'PNG':2, 'GIF':3, 'JPG':4, 'TIFF':5, 'EPS':6, 'RAW':7, 'ICO':8, }

def is_correct(file_in_memory=None):
    if file_in_memory:
        path, ext = os.path.splitext(file_in_memory.name)
        if ALLOWED_TYPES.get(ext.upper()):
            pass


class ImgUpload (APIView):
    throttle_scope = 'uploads'
    def post (self, request, format=None):
        serial=ImageSerial(data=request.data)
        if serial.is_valid() and request.data.get('file') != None:
            print(request.data.get('file'))
            suka = {'total': 1}
            return Response(data=suka, status=status.HTTP_202_ACCEPTED)
        return Response(data={'total': 0},status=status.HTTP_400_BAD_REQUEST)