from rest_framework import viewsets

from .models import Video
from .serializers import VideoSerializer, FolderSerializer, CategorySerializer
from filer.models.foldermodels import Folder
from aldryn_categories.models import Category

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class FolderViewSet(viewsets.ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
