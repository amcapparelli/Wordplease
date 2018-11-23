from django.contrib.auth.models import User
from rest_framework import serializers

class UserInfoSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()

class UserSerializer(UserInfoSerializer):

    password = serializers.CharField()

    def create(self, validated_data):
        user = User()
        return self.update(user, validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance

    def validate_username(self, value):
        if self.instance and self.instance.username != value and User.objects.filter(username=value).exists():
            raise serializers.ValidationError('Username {0} not available'.format(value))

        if self.instance is None and User.objects.filter(username=value).exists():
            raise serializers.ValidationError('Username {0} not available'.format(value))
        return value
