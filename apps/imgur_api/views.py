from django.shortcuts import render, redirect
import pyimgur

# Create your views here.
def index(request):
    CLIENT_ID = "b43f46c3df6f4ca"
    im = pyimgur.Imgur(CLIENT_ID)
    image = im.get_image('S1jmapR')
    print(image.title) # Cat Ying & Yang
    print(image.link) # http://imgur.com/S1jmapR.jpg
    context = {
        'image': image,
    }
    return render(request, 'imgur_api/index.html', context)

def landing(request):
    CLIENT_ID = "b43f46c3df6f4ca"
    im = pyimgur.Imgur(CLIENT_ID)
    image = im.get_image('S1jmapR')
    print(image.title) # Cat Ying & Yang
    print(image.link) # http://imgur.com/S1jmapR.jpg
    context = {
        'image': image,
    }
    return render(request, 'imgur_api/landing.html', context)