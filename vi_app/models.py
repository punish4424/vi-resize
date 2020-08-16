import sys
from io import BytesIO

import moviepy.editor as mp
from PIL import Image
from django.conf import settings
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models


class Story(models.Model):
    user_name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='uploads/', null=True, blank=True)
    description = models.TextField()
    type = models.CharField(max_length=50, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = 'Story'
        verbose_name_plural = 'Stories'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if 'image' in self.file.file.content_type:
            im = Image.open(self.file)
            output = BytesIO()
            im = im.resize((1200, 600))
            im.save(output, format='JPEG', quality=100)
            output.seek(0)
            self.file = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.file.name.split('.')[0],
                                             'image/jpeg',
                                             sys.getsizeof(output), None)
            self.type = "Image"
            super(Story, self).save()
            return True

        if 'video' in self.file.file.content_type:
            file_name = self.file.name
            self.type = "Video"
            super(Story, self).save()
            clip = mp.VideoFileClip(self.file.path)
            clip_resized = clip.resize(width=480)
            path = settings.MEDIA_ROOT
            clip_resized.write_videofile(codec='libx264', audio_codec='aac', filename=path + "/" + file_name)
            return True


class Resize(models.Model):
    file = models.FileField(upload_to='files/')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Resize'
        verbose_name_plural = 'Resize'

    def save(self, *args, **kwargs):
        if 'image' in self.file.file.content_type:
            im = Image.open(self.file)
            output = BytesIO()
            im = im.resize((956, 1004))
            im.save(output, format='PNG', quality=100)
            output.seek(0)
            self.file = InMemoryUploadedFile(output, 'ImageField', "%s.png" % self.file.name.split('.')[0],
                                             'image/png', sys.getsizeof(output), None)
            super(Resize, self).save()
            return True

        if 'video' in self.file.file.content_type:
            file_name = self.file.name
            super(Resize, self).save()
            clip = mp.VideoFileClip(self.file.path)
            clip_resized = clip.resize(width=480)
            path = settings.MEDIA_ROOT
            clip_resized.write_videofile(codec='libx264', audio_codec='aac', filename=path + "/" + file_name)
