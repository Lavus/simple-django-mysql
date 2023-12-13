# projects/views.py

from django.shortcuts import render
from projects.models import Project

def index(request):
    databases = ["default","localhost","RDS","otherRDS"]
    context = {
        "databases": databases
    }
    return render(request, "projects/index.html", context)

def project_index(request, source):
    projects = Project.objects.using(source).all()
    context = {
        "projects": projects,
        "source": source
    }
    return render(request, "projects/project_index.html", context)

def project_detail(request, source, pk):
    project = Project.objects.using(source).get(pk=pk)
    context = {
        "project": project
    }
    return render(request, "projects/project_detail.html", context)