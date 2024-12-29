from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from django.contrib.auth.hashers import make_password  # Importar make_password para encriptar

@api_view(['POST'])
def register_user(request):
    data = request.data
    username = data.get('username')
    password = data.get('password')

    # Validar si el usuario ya existe
    if User.objects.filter(username=username).exists():
        return Response({'error': 'El nombre de usuario ya existe.'}, status=status.HTTP_400_BAD_REQUEST)

    # Encriptar la contraseña antes de guardar
    encrypted_password = make_password(password)

    # Crear el usuario en tu modelo personalizado
    user = User.objects.create(
        username=username,
        password=encrypted_password,  # Guardar la contraseña encriptada
    )

    return Response({'message': 'Usuario creado exitosamente'}, status=status.HTTP_201_CREATED)
