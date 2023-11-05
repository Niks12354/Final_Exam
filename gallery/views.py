from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    return render(request, "home.html",{})

def photos(request):
    return render(request, "albums/photos.html",{})

def albums(request):
    image_data = [
        {
            'url': '/static/images/images1.jpg',
            'title': 'Image 1',
        },
        {
            'url': '/static/images/images2.jpg',
            'title': 'Image 2',
        },
        {
            'url': '/static/images/images3.jpg',
            'title': 'Image 3',
        },
        {
            'url': '/static/images/images4.jpg',
            'title': 'Image 4',
        },
        {
            'url': '/static/images/images5.jpg',
            'title': 'Image 5',
        },
        {
            'url': '/static/images/images6.jpg',
            'title': 'Image 6',
        },
        {
            'url': '/static/images/images7.jpg',
            'title': 'Image 7',
        },
        {
            'url': '/static/images/images8.jpg',
            'title': 'Image 8',
        },
        {
            'url': '/static/images/images9.jpg',
            'title': 'Image 9',
        },
                {
            'url': '/static/images/images10.jpg',
            'title': 'Image 10',
        },
    ]
    context = {
        'photos': image_data,
    }
    
    return render(request, "albums/index.html",context)


# def photos(request, id):
#     albumsResponse = requests.get("https://jsonplaceholder.typicode.com/albums/" + str(id))

#     photosResponse = requests.get("https://jsonplaceholder.typicode.com/photos?albumId=" + str(id))
#     data = photosResponse.json()
#     albumData = albumsResponse.json();

#     context = {
#         'photos': data,
#         'album': albumData
#     }
#     return render(request, "albums/photos.html",context)
def photos(request):
    # Manually create a list of image data with file paths
    image_data = [
        {
            'url': '/static/images/images1.jpg',
            'title': 'Image 1',
        },
        {
            'url': '/static/images/images2.jpg',
            'title': 'Image 2',
        },
        {
            'url': '/static/images/images3.jpg',
            'title': 'Image 3',
        },
        {
            'url': '/static/images/images4.jpg',
            'title': 'Image 4',
        },
        {
            'url': '/static/images/images5.jpg',
            'title': 'Image 5',
        },
        {
            'url': '/static/images/images6.jpg',
            'title': 'Image 6',
        },
        {
            'url': '/static/images/images7.jpg',
            'title': 'Image 7',
        },
        {
            'url': '/static/images/images8.jpg',
            'title': 'Image 8',
        },
        {
            'url': '/static/images/images9.jpg',
            'title': 'Image 9',
        },
        {
            'url': '/static/images/images10.jpg',
            'title': 'Image 10',
        },
    ]
    context = {
        'photos': image_data,
    }
    return render(request, "albums/photos.html", context)
