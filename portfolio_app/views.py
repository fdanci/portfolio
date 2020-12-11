from django.shortcuts import render, redirect
from shared.utils import send_contact_email

from portfolio_app.forms import ContactForm


def index(request):
    context = {}
    return render(request, 'portfolio_app/index.html', context)


def contact(request):
    context = {'form': ContactForm()}
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


def contact_me(request):
    """Receives contact information and tries to send email."""
    send_contact_email(request.POST['name'],
                       request.POST['email'],
                       request.POST['subject'],
                       request.POST['message'])
    return redirect('/contact')
