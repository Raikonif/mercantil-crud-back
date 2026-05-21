from drf_spectacular.utils import OpenApiExample, extend_schema

from manual.serializers import ManualSerializer

manual_schema = extend_schema(
    summary="Example schema for the Manual model",
    tags=["manual"],
    request=ManualSerializer,
    responses=ManualSerializer,
    examples=[
        OpenApiExample(
            "Create manual",
            summary="Create a new manual",
            value={"name": "", "description": ""},
            request_only=True,
        ),
        OpenApiExample(
            "Read manual",
            summary="Read a manual",
            value={"id": 1, "name": "", "description": ""},
            response_only=True,
        ),
        OpenApiExample(
            "Update manual",
            summary="Update a manual",
            value={"id": 1, "name": "", "description": ""},
            request_only=True,
        ),
        OpenApiExample(
            "Update manual response",
            summary="Updated manual",
            value={"id": 1, "name": "", "description": ""},
            response_only=True,
        ),
        OpenApiExample(
            "Delete manual response",
            summary="Deleted manual",
            value={"id": 1, "name": "", "description": ""},
            response_only=True,
        ),
    ],
)
