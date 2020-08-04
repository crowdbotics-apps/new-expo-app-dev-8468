from rest_framework import authentication
from homehh.models import GFhgjhgjh
from .serializers import GFhgjhgjhSerializer
from rest_framework import viewsets


class GFhgjhgjhViewSet(viewsets.ModelViewSet):
    serializer_class = GFhgjhgjhSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = GFhgjhgjh.objects.all()
