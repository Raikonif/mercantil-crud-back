from rest_framework.viewsets import ModelViewSet

from manual.models import Manual
from manual.schemas import manual_schema
from manual.serializers import ManualSerializer


@manual_schema
class ManualViewSet(ModelViewSet):
    queryset = Manual.objects.all().order_by("-id")
    serializer_class = ManualSerializer
