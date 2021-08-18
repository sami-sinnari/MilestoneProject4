from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def accordion(request):

    context = {
        'accordion_page': 'active',
    }

    return render(request, 'home/accordion.html', context)