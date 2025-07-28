from rest_framework import serializers


class FileSizeValidator():
    def __init__(self, max_size_mb):
        self.max_size_mb = max_size_mb

    def __call__(self, value):
        size = getattr(value, 'size', 0)

        if size > self.max_size_mb:
            message = f"The file uploaded must be less than {self.max_size_mb} MB"
            raise serializers.ValidationError(message)


class FileTypeValidator():
    def __init__(self, allowed_types=None):
        if allowed_types is None:
            allowed_types = ['image/jpeg', 'image/png', 'image/webp']
        self.allowed_types = allowed_types

    def __call__(self, value):
        content_type = getattr(value, 'content_type', None)

        if content_type not in self.allowed_types:
            message = f"The file uploaded must be one of {self.allowed_types}"
            raise serializers.ValidationError(message)
