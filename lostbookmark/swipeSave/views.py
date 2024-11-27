import requests
from django.shortcuts import render
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.decorators import login_required


@login_required
def bookmark_list(request, format=None):
    try:
        # Get Twitter account info
        social_account = SocialAccount.objects.get(
            user=request.user,
            provider='twitter_oauth2'
        )

        twitter_user_id = social_account.uid

        if request.method == 'GET':
            print('this is the get request')
            r = requests.get(
                f'https://api.x.com/2/users/{twitter_user_id}/bookmarks',
                params=request.GET
            )
            print(r.json())
            return render(request, 'swipeSave/swipeInterface.html', {'bookmarks': r.json()})

        elif request.method == 'POST':
            print('this is the post request')
            # Your POST handling code here

        elif request.method == 'DELETE':
            print('this is the delete request')
            # Your DELETE handling code here

    except SocialAccount.DoesNotExist:
        return render(request, 'swipeSave/swipeInterface.html',
                      {'error': 'No Twitter account connected'})


@login_required
def swipe_interface(request):
    try:
        # Get Twitter account info
        social_account = SocialAccount.objects.get(
            user=request.user,
            provider='twitter_oauth2'
        )

        twitter_user_id = social_account.uid
        twitter_data = social_account.extra_data

        context = {
            'twitter_user_id': twitter_user_id,
            'twitter_data': twitter_data,
        }

        return render(request, 'swipeSave/swipeInterface.html', context)

    except SocialAccount.DoesNotExist:
        return render(request, 'swipeSave/swipeInterface.html',
                      {'error': 'No Twitter account connected'})
