from django.urls import include, path

urlpatterns = [
    path("", include("manual.urls")),
    path("", include("api.urls")),
]
