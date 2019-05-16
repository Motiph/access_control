from rest_framework import serializers

from .models import AllowedHost, WhiteListItem


class AllowedHostSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllowedHost
        fields = '__all__'


class WhiteListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhiteListItem
        fields = '__all__'
