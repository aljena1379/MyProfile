from django.shortcuts import render

def profilePreview(request):
    return render(request, 'preview.html')