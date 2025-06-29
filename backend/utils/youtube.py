import requests

from django.core.cache import cache

from backend.settings.base import YOUTUBE_API_URL, YOUTUBE_REQUEST_HEADERS  # TODO:以后解决一下请求头导入的有效性问题


CACHE_KEY = [
    'youtube_data:channel_stats',
]


def fetch_youtube_data():
    """Fetch YouTube Data and Update Cache"""

    header, url = YOUTUBE_REQUEST_HEADERS, YOUTUBE_API_URL
    response = requests.get(url, headers=header)
    data = response.json()

    cache.set(CACHE_KEY[0], data, timeout=None)
