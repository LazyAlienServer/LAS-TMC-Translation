from django.core.cache import cache


def key(*parts):
    """
    Generate a standard cache key. All cache keys should be generated using this function.

    e.g. key("article", "slug", slug) -> "article:slug:name-of-the-article"
    """
    # Convert all parts into string, join them with ':'.
    return ":".join(str(p) for p in parts)


def get_cache(*parts):
    k = key(*parts)

    return cache.get(k)


def set_cache(*parts, value, timeout=None):
    k = key(*parts)

    return cache.set(k, value, timeout=timeout)


def delete_cache(*parts):
    k = key(*parts)

    return cache.delete(k)


def get_or_set_cache(*parts, creator, timeout=None):
    """
    Retrieves a key value from the cache and sets the value if it does not exist.
    """
    k = key(*parts)
    return cache.get_or_set(k, creator, timeout=timeout)


def delete_cache_pattern(*pattern_parts, version=None):
    k = key(*pattern_parts)
    return cache.delete_pattern(k, version=version)
