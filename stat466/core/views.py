from django.shortcuts import render


def index(request):
    params = {}
    return render(request, 'core/index.html', params)
