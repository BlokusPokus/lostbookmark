from django.shortcuts import render
from django.http import HttpResponse
from allauth.socialaccount.models import SocialAccount

# Create your views here.


def home(request):
    return render(request, 'SocialAuth/index.html')
# step 3 : create a login view


def login(request):
    return render(request, 'SocialAuth/login.html')


def dashboard(request):
    if request.user.is_authenticated:
        try:
            social_account = SocialAccount.objects.get(
                user=request.user, provider='twitter_oauth2')
            twitter_user_id = social_account.uid
            extra_data = social_account.extra_data

            context = {
                'twitter_user_id': twitter_user_id,
                'extra_data': extra_data
            }
            return render(request, 'SocialAuth/dashboard.html', context)
        except SocialAccount.DoesNotExist:
            return render(request, 'SocialAuth/dashboard.html',
                          {'error': 'No Twitter account connected'})

    return render(request, 'SocialAuth/dashboard.html')


def clean_bookmark(request):
    return HttpResponse("Clean Bookmark")
