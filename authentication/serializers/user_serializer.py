from rest_framework import serializers
from authentication.models.user import CustomUser


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField()
    full_name = serializers.CharField()
    phone_number = serializers.CharField()
    avatar_url = serializers.CharField()
    bio = serializers.CharField()

    class Meta:
        model = CustomUser
        fields = (
            'id',
            'email',
            'full_name',
            'bio',
            'phone_number',
            'avatar_url')
        extra_kwargs = {
            'id': {'read_only': True},
            'email': {'read_only': True},
            'full_name': {'read_only': True},
            'bio': {'read_only': True},
            'phone_number': {'read_only': True},
            'avatar_url': {'read_only': True},
        }
