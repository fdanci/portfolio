from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'portfolio_app/index.html', context)


def contact(request):
    context = {}
    return render(request, 'portfolio_app/contact.html', context)


def about_me(request):
    context = {}
    return render(request, 'portfolio_app/about_me.html', context)


def hobbies(request):
    context = {}
    return render(request, 'portfolio_app/hobbies.html', context)


def work(request):
    context = {}
    return render(request, 'portfolio_app/work.html', context)
