from django.shortcuts import render, redirect

from portfolio_app.models import Drawing
from shared.utils import send_contact_email
from portfolio_app.forms import ContactForm
from django.contrib import messages


def index(request):
    context = {
        'header': ''
    }
    return render(request, 'portfolio_app/index.html', context)


def contact(request):
    context = {'form': ContactForm(), 'header': 'Contact'}
    return render(request, 'portfolio_app/contact.html', context)


def about_me(request):
    context = {'header': 'About Me'}
    return render(request, 'portfolio_app/about_me.html', context)


def hobbies(request):
    drawing_urls = [drawing.url for drawing in Drawing.objects.all()]
    context = {
        'header': 'Hobbies',
        'drawings': drawing_urls
    }

    return render(request, 'portfolio_app/hobbies.html', context)


def work(request):
    context = {'header': 'Work Experience'}
    return render(request, 'portfolio_app/work.html', context)


def contact_me(request):
    """Receives contact information and tries to send email."""
    send_contact_email(request.POST['name'],
                       request.POST['email'],
                       request.POST['subject'],
                       request.POST['message'])
    messages.success(request, 'Your message was received!')
    return redirect('/contact')