from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'portfolio_app/index.html', context)
