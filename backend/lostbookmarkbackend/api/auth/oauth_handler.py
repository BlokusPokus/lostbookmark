# Move from backend/api/auth/oauth_handler.py to backend/lostbookmarkbackend/api/auth/oauth_handler.py
# Content remains the same

from typing import Dict, Optional
import tweepy
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class OAuthHandler:
    def __init__(self):
        self.oauth_config = {
            'twitter': {
                'client_id': os.getenv('TWITTER_CLIENT_ID'),
                'client_secret': os.getenv('TWITTER_CLIENT_SECRET'),
                'redirect_uri': os.getenv('TWITTER_REDIRECT_URI'),
                'scope': ['tweet.read', 'users.read', 'bookmark.read']
            },
            'youtube': {
                'client_id': os.getenv('YOUTUBE_CLIENT_ID'),
                'client_secret': os.getenv('YOUTUBE_CLIENT_SECRET'),
                'redirect_uri': os.getenv('YOUTUBE_REDIRECT_URI'),
                'scope': ['https://www.googleapis.com/auth/youtube']
            }
        }

    async def handle_twitter_oauth(self, code: str) -> Dict:
        """Handle Twitter OAuth flow"""
        try:
            # Initialize Tweepy OAuth2 handler
            oauth2_user_handler = tweepy.OAuth2UserHandler(
                client_id=self.oauth_config['twitter']['client_id'],
                client_secret=self.oauth_config['twitter']['client_secret'],
                redirect_uri=self.oauth_config['twitter']['redirect_uri'],
                scope=self.oauth_config['twitter']['scope']
            )

            # Exchange the code for access token
            access_token = oauth2_user_handler.fetch_token(code)

            # Create client with access token
            client = tweepy.Client(access_token['access_token'])

            # Get user information
            user = client.get_me()

            return {
                'access_token': access_token['access_token'],
                'refresh_token': access_token.get('refresh_token'),
                'user_id': user.data.id,
                'username': user.data.username
            }

        except Exception as e:
            raise Exception(f"Twitter OAuth error: {str(e)}")

    async def handle_youtube_oauth(self, code: str) -> Dict:
        """Handle YouTube OAuth flow"""
        pass

    async def refresh_token(self, service: str, refresh_token: str) -> Optional[str]:
        """Refresh OAuth tokens"""
        if service != 'twitter':
            return None

        try:
            oauth2_user_handler = tweepy.OAuth2UserHandler(
                client_id=self.oauth_config['twitter']['client_id'],
                client_secret=self.oauth_config['twitter']['client_secret'],
                redirect_uri=self.oauth_config['twitter']['redirect_uri']
            )

            new_token = oauth2_user_handler.refresh_token(refresh_token)
            return new_token['access_token']
        except Exception:
            return None
