from django.contrib import admin
from filer.admin.fileadmin import FileAdmin

from .models import Video

class VideoAdmin(FileAdmin):
    pass

VideoAdmin.fieldsets = VideoAdmin.build_fieldsets(
    extra_main_fields=('categories', 'metadata',)
)

admin.site.register(Video, VideoAdmin)
