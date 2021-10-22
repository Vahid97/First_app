from django.shortcuts import render
from .models import Project


def projects(request):
    # Neye gore onceden butun projectsleri goturmeliyik
    projects = Project.objects.all()

    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        projects = Project.objects.filter(title=search_query)

    
    context = {'projects':projects}

    return render(request, 'projects/projects.html', context)



def project(request, pk):
    project = Project.objects.get(id=pk)
    reviews = project.review_set.all()

    context = {'projectObj':project, 'reviews':reviews}
    return render(request, 'projects/single-project.html', context)








    
