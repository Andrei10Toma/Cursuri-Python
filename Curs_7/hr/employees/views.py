from django.shortcuts import render


def homepage(request):
    return render(request, "homepage.html", {
        "name": "Andrei",
        "fw_name": "Django",
    })
