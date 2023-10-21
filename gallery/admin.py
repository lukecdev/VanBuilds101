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
        for image_submission in queryset:
            image = Image(image=image_submission.image)
            image.save()
            queryset.update(approved=True)
            image_submission.delete()

        self.message_user(request, f'Selected images have been approved and moved to "admin/gallery/image/".') 

admin.site.register(ImageSubmission, ImageSubmissionAdmin)
