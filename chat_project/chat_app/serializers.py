from rest_framework import serializers
from . models import chatmessage

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = chatmessage
        fields = ['textmsg']
