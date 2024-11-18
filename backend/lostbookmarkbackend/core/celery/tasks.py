# Move from backend/core/celery/tasks.py to backend/lostbookmarkbackend/core/celery/tasks.py
# Content remains the same
from celery import Celery
from typing import List

app = Celery('lostbookmark')


@app.task
def process_batch_deletion(service: str, item_ids: List[str], user_id: str):
    """Background task for batch deletion"""
    pass


@app.task
def refresh_user_content(user_id: str):
    """Background task to refresh user's content"""
    pass
