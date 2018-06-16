from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template


def index(request):
    return render(request, 'frontend/index.html')

def projects(request):
    return render(request, 'frontend/projects.html')

def contact(request):
    form_class = ContactForm


    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'full_name'
            , '')
            contact_email = request.POST.get(
                'email_address'
            , '')
            form_content = request.POST.get('comments', '')

            # Email the profile with the
            # contact information
            template = get_template('frontend/contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Web Portfolio" +'',
                ['danebrwn47@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('contact')

    return render(request, 'frontend/contact.html', {
        'form': form_class,
    })
