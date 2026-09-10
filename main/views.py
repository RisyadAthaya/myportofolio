from django.shortcuts import render
from main.models import Experience

def show_main(request):
    context = {
        "name": "Risyad Athaya Muhammad",
        "nickname": "Athaya",
        "npm": "2506595890",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "An undergraduate Information Systems student at the University of Indonesia. "
            "Currently trying to learn software engineering, exploring opportunities, and actively pursuing knowledge."
        ),
    }
    return render(request, "index.html", context)

def show_experience(request):
    context = {
        "name": "Risyad Athaya Muhammad",
        "nickname": "Athaya",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_projects(request):
    context = {
        "nickname": "Athaya",
    }
    return render(request, "projects.html", context)