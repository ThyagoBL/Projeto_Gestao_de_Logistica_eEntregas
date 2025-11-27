# contas/views.py (Código para Registro e Login)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer  # Nosso validador de dados

# ----------------------------------------------------
# VISÃO DE REGISTRO
# ----------------------------------------------------
class RegisterView(APIView):
    # O método 'post' será chamado quando houver um POST para /api/auth/register
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        
        # O Serializer.is_valid() faz toda a validação de dados
        if serializer.is_valid():
            # serializer.save() chama o método create que criamos, criptografando a senha
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # Retorna erros detalhados se a validação falhar
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ----------------------------------------------------
# VISÃO DE LOGIN (Próximo Passo)
# ----------------------------------------------------
class LoginView(APIView):
    def post(self, request):
        # A lógica de login real (com token JWT) será implementada aqui.
        return Response({"message": "Login pronto para JWT!"}, status=status.HTTP_200_OK)