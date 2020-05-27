from django.contrib.sites.shortcuts import get_current_site
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from vi_app import serializer
from vi_app.models import Story, Resize
from vi_app.serializer import ImageorVideoSerializer


class ImageUploadAPIView(viewsets.ModelViewSet):
    serializer_class = serializer.ImageUploadSerializer
    queryset = Story.objects.all()


class ImageORVideoResize(APIView):
    serializer_class = ImageorVideoSerializer

    # def get(self, request, *args, **kwargs):
    #     serializer = self.serializer_class(Resize.objects.all(), many=True)
    #     return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        file_name = request.FILES.get('file').name
        if 'image' in request.FILES.get('file').content_type:
            file_type = 'Image'
        elif 'video' in request.FILES.get('file').content_type:
            file_type = 'Video'
        file = Resize.objects.create(file=request.FILES.get('file'))
        site = get_current_site(request)
        if file_type == 'Image':
            url = request.stream.scheme + "://" + site.domain + "/media/" + file.file.name
            return Response({"url": url})
        url = request.stream.scheme + "://" + site.domain + "/media/" + file_name
        return Response({"url": url})
