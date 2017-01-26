from django.shortcuts import render
from rango.models import Category
from rango.models import Page
from django.http import HttpResponse

def index(request):
    #Query for categories and sort by amt of likes in decending order
    #and only get the top 5
    category_list = Category.objects.order_by('-likes')[:5]
    #same for pages
    page_list  = Page.objects.order_by('-views')[:5]
    # Construct a dictionary to pass to the template engine as its context.
    context_dict = {'categories': category_list, 'pages' : page_list}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return render(request, 'rango/about.html', {})

def friends(request):
    context_dict = {'boldmessage': 'Guess who is a cat! Click on an image to guess.',
                    'queen': 'No, HM Queen Elisabeth II is clearly a human.',
                    'nigiri' : 'Yes, Nigiri is indeed a cat.',
                    'pope': 'No, the pope is really a dog dressed up as The Pope.',
                    'bunny' : 'No, the Easter Bunny is a bunny!',
                    'kitty' : 'Yes, Miss Kitty is a cat.',
                    'cat' : 'No, Mommy Cat is not really a cat. She is a human.',
                    }
    return render(request, 'rango/friends.html', context=context_dict)

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)

        pages = Page.objects.filter(category=category)

        context_dict ['pages'] = pages

        context_dict ['category'] = category

    except Category.DoesNotExist:

        context_dict['category'] = None

        context_dict['pages'] = None

    return render(request, 'rango/category.html', context_dict)