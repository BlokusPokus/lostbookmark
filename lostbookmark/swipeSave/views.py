
from rest_framework.decorators import api_view
import requests
from django.http import HttpResponse
from django.shortcuts import render


@api_view(['GET', 'POST'])
def bookmark_list(request, format=None):
    if request.method == 'POST':
        print('this is the post request')

        # r = requests.post(
        #     'https://api.x.com/2/users/:id/bookmarks', params=request.POST)
    elif request.method == 'GET':
        print('this is the get request')
        mock_data = {
            'url': 'https://example.com',
            'title': 'Example Website',
            'description': 'This is a sample website description'
        }
        return HttpResponse(mock_data)
        # r = requests.get(
        #     'https://api.x.com/2/users/:id/bookmarks', params=request.GET)
    elif request.method == 'DELETE':
        print('this is the delete request')
        # r = requests.delete(
        #     'https://api.x.com/2/users/:id/bookmarks', params=request.DELETE)
    # if r.status_code == 200:
    #     return HttpResponse('Yay, it worked')
    # return HttpResponse('Could not save data')


def swipe_interface(request):
    return render(request, 'swipeSave/swipeInterface.html')
