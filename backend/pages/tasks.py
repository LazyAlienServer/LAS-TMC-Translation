from celery import shared_task
from core.utils.youtube import fetch_youtube_data


@shared_task
def refresh_youtube_cache():
    try:
        fetch_youtube_data()
        return {"status": "success", "message": "YouTube channel data successfully refreshed"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
