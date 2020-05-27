from rest_framework import serializers

from vi_app.models import Story, Resize


class ImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = '__all__'


class ImageorVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resize
        fields = '__all__'
