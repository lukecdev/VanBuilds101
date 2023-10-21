from django.shortcuts import render, redirect
from .models import Image

def van_images(request):
    images = Image.objects.all()
    
    return render(
            request,
            "van_images.html",
            {'images': images}
        )

def submit_image(request):
    if request.method == 'POST':
        data = request.POST
        images = request.FILES.get('image')

        print('image:', image)
    
    #if request.method == 'POST':
     #   form = ImageSubmissionForm(request.POST, request.FILES)
      #  if form.is_valid():
       #     form.save()
        #    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

    else:
        form = ImageSubmissionForm()        

    return render(request, "van_images.html", {'images': images})


