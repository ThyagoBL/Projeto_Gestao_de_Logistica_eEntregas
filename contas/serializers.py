# contas/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    # O Django exige que a senha seja tratada de forma especial para criptografia
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        # Os campos que a API pode receber e retornar
        fields = ('id', 'username', 'email', 'password')
        # Garante que a senha não seja retornada na resposta JSON
        extra_kwargs = {'password': {'write_only': True}} 

    # Sobrescreve a função de criação para criptografar a senha
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', validated_data['username']),
            password=validated_data['password']
        )
        return user