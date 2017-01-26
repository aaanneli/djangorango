from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}

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
