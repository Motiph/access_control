from django.shortcuts import render
from .models import AllowedHost, WhiteListItem
from .mixins import DefaultViewSetMixin, ModelViewSetMixin
from .serializers import AllowedHostSerializer, WhiteListItemSerializer

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class AllowedHostViewSet(DefaultViewSetMixin, ModelViewSetMixin):
    permission_classes = (IsAuthenticated,)
    queryset = AllowedHost.objects.all()
    serializer_class = AllowedHostSerializer


class WhiteListItemViewSet(DefaultViewSetMixin, ModelViewSetMixin):
    permission_classes = (IsAuthenticated,)
    queryset = WhiteListItem.objects.all()
    serializer_class = WhiteListItemSerializer
