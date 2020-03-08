from rest_framework import  serializers
from first import models

class UserProfileSerializer(serializers.ModelSerializer):
    """serializer for user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
            'write_only': True,
            'style': {'imput_type': 'password'}
            }
        }

    def create(self, validated_data):
        """create a new user """

        user = models.UserProfile.objects.create_user(
        email=validated_data['email'],
        name=validated_data['name'],
        password=validated_data['password']
        )
        return user