from django.conf.urls import url
from rest_framework import routers
from .views import VideoViewSet, FolderViewSet, CategoryViewSet


from djangocms_rest_api.views import PageViewSet, PlaceHolderViewSet, PluginViewSet


router = routers.DefaultRouter()
router.register(r'videos', VideoViewSet)
router.register(r'folder', FolderViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'pages', PageViewSet, 'page')
router.register(r'placeholders', PlaceHolderViewSet, 'placeholder')
router.register(r'plugins', PluginViewSet, 'plugin')

urlpatterns = router.urls
