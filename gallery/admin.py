from django.contrib import admin
from .models import Image

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'approved']
    search_fields = ['title', 'author']
    list_filter = ('approved',)
    actions = ['approve_images']

    def approve_images(self, request, queryset):
        queryset.update(approved=True)

        self.message_user(request, f'Selected images have been approved')