from rest_framework.views import exception_handler
from rest_framework import status


def extract_toast_error(data):
    first_error = next(iter(data.values()))

    if isinstance(first_error, list):
        first_error = first_error[0]

    return first_error


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        toast_error = extract_toast_error(response.data)
        response.data['toast_error'] = toast_error
        response.data['success'] = status.is_success(response.status_code)

    return response
