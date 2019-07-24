

from django.shortcuts import render
from .models import Album

# Create your views here.

from django.http import HttpResponse

def index(request):
    all_albums = Album.objects.all()
    html = ''
    for album in all_albums:
        url = '/music/' + str(album.id) + '/'
        html += '<a href=" ' + url + ' ">' + album.album_title + '</a><br>'
    return HttpResponse(html)

def detail(request, album_id):
    return HttpResponse("<h2>DETAILS FOR ALBUM ID: "+ str(album_id) + "</h2>")

def harsh (request):
	return HttpResponse("<h1>Hum aa gye</h1>")

def printdata(request):
	print(request)
	if request.method =='GET':
		name=request.GET['fname']
	print(name)
	return HttpResponse("Hello")

