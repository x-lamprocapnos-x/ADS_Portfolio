from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from .models import Project

# Create your views here.

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extract cleaned data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Construct email content
            subject = f'New Contact Form Submission from {name}'
            full_message = f'From {name} <{email}>\n\nMessage:\n{message}'

            # Send email to your gmail
            send_mail(
                subject,
                full_message,
                settings.EMAIL_HOST_USER, # From
                [settings.EMAIL_HOST_USER], # To
                fail_silently=False,
            )

            return render(request, 'main/contact_success.html', {'name': name})
    else:
        form = ContactForm()

    return render(request, 'main/contact.html', {'form': form})

def projects(request):
    all_projects = Project.objects.all()
    return render(request, 'main/projects.html', {'projects': all_projects})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'main/project_detail.html', {'project': project})