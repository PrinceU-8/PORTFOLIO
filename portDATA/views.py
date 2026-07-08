from django.shortcuts import render, get_object_or_404
from .models import ProjDATA, PersonDATA

def about(request):
    personal_info = PersonDATA.objects.first()
    return render(request, 'about.html', {'profile': personal_info})

def project_list(request):
    projects = ProjDATA.objects.all()
    return render(request, 'works.html', {'ProjDATA': projects})

def project_detail(request, project_id):
    project = get_object_or_404(ProjDATA, pk=project_id)
    return render(request, 'project_detail.html', {'project': project})