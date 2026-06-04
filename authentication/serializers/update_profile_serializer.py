from rest_framework import serializers
from authentication.models.user import CustomUser


class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'full_name',
            'avatar_url',
            'bio',
            'phone_number',
        )
        extra_kwargs = {
            'full_name': {'required': False, 'allow_blank': True},
            'avatar_url': {'required': False, 'allow_blank': True},
            'bio': {'required': False, 'allow_blank': True},
            'phone_number': {'required': False, 'allow_blank': True},
        }

    def validate(self, attrs):
        if attrs.get('full_name') is not None:
            attrs['full_name'] = attrs['full_name'].strip()
        if attrs.get('avatar_url') is not None:
            attrs['avatar_url'] = attrs['avatar_url'].strip()
        if attrs.get('bio') is not None:
            attrs['bio'] = attrs['bio'].strip()
        if attrs.get('phone_number') is not None:
            attrs['phone_number'] = attrs['phone_number'].strip()
        return attrs

    def update(self, instance, validated_data):
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.avatar_url = validated_data.get('avatar_url', instance.avatar_url)
        instance.save()
        return instance
