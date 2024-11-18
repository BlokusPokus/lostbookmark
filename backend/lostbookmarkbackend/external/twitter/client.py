# Move from backend/external/twitter/client.py to backend/lostbookmarkbackend/external/twitter/client.py
# Content remains the same
from typing import List, Dict


class TwitterClient:
    def __init__(self, access_token: str):
        self.access_token = access_token

    async def fetch_bookmarks(self, user_id: str) -> List[Dict]:
        """Fetch user's Twitter bookmarks"""
        pass

    async def delete_bookmark(self, bookmark_id: str) -> bool:
        """Delete a single bookmark"""
        pass

    async def batch_delete_bookmarks(self, bookmark_ids: List[str]) -> Dict:
        """Delete multiple bookmarks"""
        pass
