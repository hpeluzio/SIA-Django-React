from django.contrib.auth import password_validation
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import CustomUser


class TokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Token
        fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):

    # auth_token = TokenSerializer()

    class Meta:
        model = CustomUser
        # fields = ('email', 'password')
        fields = '__all__'
        # write_only_fields = ('password',)
        extra_kwargs = {'password': {'write_only': True}}
        # exclude = ('password',)

    # def create(self, validated_data):
        # user = CustomUser.objects.create(
        #     email=validated_data['email'], password=validated_data['password'])
        # return user
        # user = CustomUser()
        # user.email = validated_data['email']
        # user.set_password(validated_data['password'])
        # user.save()
        # return user
        # user = CustomUser.objects.create(
        #     email=validated_data['email']
        # )
        # user.set_password(validated_data['password'])
        # user.save()

        # return user

    # def validate(self, data):
    #     print(data)
    #     password = data.get('confirm_password')
    #     confirm_password = data.get('confirm_password')
    #     if password != confirm_password:
    #         raise serializers.ValidationError(
    #             {"ValidationError": data})
    #     return data

    def validate_password(self, value):
        password_validation.validate_password(value, self.instance)
        return value
