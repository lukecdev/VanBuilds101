from django.contrib import admin
from .models import Image, ImageSubmission

class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']

admin.site.register(Image, ImageAdmin)

class ImageSubmissionAdmin(admin.ModelAdmin):
    list_display = ('image', 'submitted_at', 'approved')
    list_filter = ('approved',)
    actions = ['approve_images']

    def approve_images(self, request, queryset):
        queryset.update(approved=True)

admin.site.register(ImageSubmission, ImageSubmissionAdmin)