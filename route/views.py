from django.shortcuts import render

# Create your views here.


def index(request):

    return render(request, 'Pages/index.html')

def about(request):

    return render(request, 'Pages/about.html')

def services(request):

    return render(request, 'Pages/services.html')

def project(request):

    return render(request, 'Pages/project.html')

def project_details(request):

    return render(request, 'Pages/project-details.html')

def contact(request):

    return render(request, 'Pages/contact.html')