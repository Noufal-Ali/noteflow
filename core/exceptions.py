import logging
from rest_framework.views import exception_handler
from rest_framework.response import Response
from core.error_codes import ERROR_CODES
from django.conf import settings

logger = logging.getLogger(__name__)

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is None:
        logger.error(f"Unhandled exception: {exc}")

        return Response({
            "error":{
                "error_code": 9999,
                "message": "Internal server error",
        }}, status=500)
    
    if isinstance(response.data, dict):
        field_errors = {}

        for field, errors in response.data.items():
            message = errors[0] if isinstance(errors, list) else str(errors)

            if field == "email":
                code = ERROR_CODES.get("EMAIL_EXISTS", 2000)
            elif field == "username":
                code = ERROR_CODES.get("USERNAME_REQUIRED", 2002)
            else:
                code = ERROR_CODES["VALIDATION_ERROR"]

            field_errors[field] = {
                "error_code": code,
                "message": message
            }

        logger.error(f"Validation error: {field_errors}")
        return Response ({
            "error":{
                "error_code": ERROR_CODES["VALIDATION_ERROR"],
                "message": "Validation error",
                "field_errors": field_errors
            }
        }, status=response.status_code)
    
    logger.error(f"Validation error: {field_errors}")
    return Response ({
        "error":{
            "error_code": ERROR_CODES["VALIDATION_ERROR"],
            "message": response.data.get("detail", "An error occurred")
        }
    }, status=response.status_code)