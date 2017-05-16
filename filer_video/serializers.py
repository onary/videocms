from rest_framework import serializers
from .models import Video
from filer.models.foldermodels import Folder
from aldryn_categories.models import Category


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video

class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
