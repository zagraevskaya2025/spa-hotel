from django.contrib import admin
from .models import GalleryImage, Page, Feedback, Service

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'description_preview', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)

    def description_preview(self, obj):
        return obj.description[:100] + '...' if len(obj.description) > 100 else obj.description
    description_preview.short_description = 'Описание'

# Регистрируем остальные модели
admin.site.register(Page)
admin.site.register(Feedback)
admin.site.register(Service) 