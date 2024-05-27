from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import *  
from .forms import ContactForm

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def macros(request):
    projects = Macro_Project.objects.all()  # Fetch all projects from the database
    context = {'projects': projects}  # Add the projects to the context
    return render(request, 'core/macros.html', context)

def scripts(request):
    projects = Script_Project.objects.all()  # Fetch all projects from the database
    context = {'projects': projects}  # Add the projects to the context
    return render(request, 'core/scripts.html', context)

def websites(request):
    projects = Website_Project.objects.all()  # Fetch all projects from the database
    context = {'projects': projects}  # Add the projects to the context
    return render(request, 'core/websites.html', context)

def education(request):
    projects = Education_Project.objects.all()  # Fetch all projects from the database
    context = {'projects': projects}  # Add the projects to the context
    return render(request, 'core/education.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Fetch the contact email from the database
            try:
                site_config = SiteConfiguration.objects.get()
                recipient_email = site_config.contact_email
            except SiteConfiguration.DoesNotExist:
                # Handle the case where the configuration doesn't exist yet
                recipient_email = 'default@example.com'  # Or raise an exception

            send_mail(
                subject,
                f'Message from {name} ({email}):\n\n{message}',
                email,  # From the user who filled out the form
                [recipient_email],
                fail_silently=False,
            )
            return redirect('contact_success')
    else:
        form = ContactForm()

    return render(request, 'core/contact.html', {'form': form})

def contact_success(request):
    return render(request, 'core/contact_success.html')  # Create this template


