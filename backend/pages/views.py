from django.core.cache import cache

from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from core.utils.youtube import CACHE_KEY

from datetime import datetime


def days_since_start(date="2023-03-17"):
    now = datetime.now()
    delta = now - datetime.strptime(date, "%Y-%m-%d")
    return delta.days


def fetch_youtube_cache():
    """Fetch cached YouTube data"""

    raw_data = cache.get(CACHE_KEY[0])
    data = raw_data["items"][0]

    return data


class YoutubeSnapshotView(APIView):
    """Return YouTube Channel Snapshot"""

    permission_classes = (AllowAny,)

    def get(self, request):

        data = fetch_youtube_cache()

        if data:
            thumbnail_url = data["snippet"]["thumbnails"]["high"]["url"]
            subscriber_count = data["statistics"]["subscriberCount"]
            video_count = data["statistics"]["videoCount"]
            view_count = data["statistics"]["viewCount"]

            return Response({
                "thumbnail_url": thumbnail_url,
                "subscriber_count": subscriber_count,
                "video_count": video_count,
                "view_count": view_count,
                "since": days_since_start(),
            })
        else:
            return Response({"error": "No data found in cache"})
