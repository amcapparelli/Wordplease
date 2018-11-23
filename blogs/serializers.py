from rest_framework import serializers


class BlogsViewSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    blog_title = serializers.CharField()