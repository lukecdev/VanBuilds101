from django.contrib import admin
from .models import Image , Imagesubmit

class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']

@admin.site.register(Image, ImageAdmin)


@admin.register(Imagesubmit)
class ImagesubmitAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_images']

    def approve_image(self, request, queryset):
        queryset.update(approved=True)