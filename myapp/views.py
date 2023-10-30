from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    return render(request, "home.html",{})

def albums(request):
    response = requests.get("https://jsonplaceholder.typicode.com/albums")
    data = response.json()
    context = {
        'albums': data
    }
    return render(request, "albums/index.html",context)


def photos(request, id):
    albumsResponse = requests.get("https://jsonplaceholder.typicode.com/albums/" + str(id))

    photosResponse = requests.get("https://jsonplaceholder.typicode.com/photos?albumId=" + str(id))
    data = photosResponse.json()
    albumData = albumsResponse.json();

    context = {
        'photos': data,
        'album': albumData
    }
    return render(request, "albums/photos.html",context)