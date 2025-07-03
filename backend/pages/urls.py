from django.urls import path

from .views import (
    YoutubeSnapshotView,
)

urlpatterns = [
    path('youtube_channel_snapshot', YoutubeSnapshotView.as_view(), name='youtube_channel_snapshot'),
]
