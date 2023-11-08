from django.shortcuts import render, request
from .models import Image
from .forms import UploadForm

def upload_image(request):
	if request.method == 'POST':
		this_form=UploadForm(request.POST, request.FILES)
		if this_form.is_valid():
			this_form.save()
			return redirect('/')
	else:
		this_form=UploadForm()
		return render(request, 'uploadImg.html', {'form':this_form})

ded view_images(request):
	all_images=Image.objects.all()
	return render(request, 'viewImages.html', {'images':all_images})
