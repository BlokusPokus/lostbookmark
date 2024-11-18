# Move from backend/external/youtube/client.py to backend/lostbookmarkbackend/external/youtube/client.py
# Content remains the same
from typing import List, Dict


class YouTubeClient:
    def __init__(self, access_token: str):
        self.access_token = access_token

    async def fetch_saved_videos(self, max_results: int = 50) -> List[Dict]:
        """Fetch user's saved videos"""
        pass

    async def delete_saved_video(self, video_id: str) -> bool:
        """Remove video from Watch Later"""
        pass

    async def batch_delete_videos(self, video_ids: List[str]) -> Dict:
        """Remove multiple videos from Watch Later"""
        pass
