class ServiceError(Exception):
    """
    The base exception class for service layer.
    """
    pass


class StateTransitionError(ServiceError):
    """
    The current status does not allow a certain type of action.

    e.g. Cannot use APPROVE when the article is PENDING
    """
    pass


class CoolingDownError(ServiceError):
    """
    The action is still cooling down.

    e.g. The CD of re-submitting an article for moderation.
    """
    pass


class NoChangeError(ServiceError):
    """
    The article must be edited before re-submitted
    """
    pass
