from rest_framework import serializers


class PostSerializers(serializers.Serializer):
    id = serializers.CharField()
    post_title = serializers.CharField()
    post_body = serializers.CharField()
    date_published = serializers.DateTimeField(format="%d-%m-%YT%H:%M")