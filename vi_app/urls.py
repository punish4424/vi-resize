from django.urls import path
from rest_framework.routers import DefaultRouter

from vi_app import views

router = DefaultRouter()
router.register('story', views.ImageUploadAPIView, basename='story')

urlpatterns = [
    path('resize/', views.ImageORVideoResize.as_view(), name='resize')
]

urlpatterns += router.urls
