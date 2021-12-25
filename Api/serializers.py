from rest_framework import serializers

from travello.models import Destination


class mySerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = ['name', 'title', 'img_url', ]
