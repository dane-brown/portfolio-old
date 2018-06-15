from django.shortcuts import render
from django.http import HttpResponse, Http404
import json

def index(request):
    return render(request, 'frontend/index.html')

def projects(request):
    return render(request, 'frontend/projects.htmwl')

def contact(request):
    return render(request, 'frontend/contact.html')


def process_form(request):
    if request.method == 'POST':
        post_text = request.POST.get('the_post')
        response_data = {}

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )

    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
