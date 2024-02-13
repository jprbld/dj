from django.shortcuts import render, redirect
from .utils import get_all_custom_models
from uploads.models import Upload

# Create your views here.

def import_data(request):
    if request.method == 'POST':
        file_path = request.FILES.get('file_path')
        model_name = request.POST.get('model_name')
        
        #store this file inside the Upload model
        upload = Upload.objects.create(
            file=file_path,
            model_name=model_name
        )

        return redirect('import_data')

    else:
        custom_models = get_all_custom_models()
        context = {
            'custom_models': custom_models
        }

    return render(request, 'dataentry/importdata.html', context)