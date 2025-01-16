from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer


class CadastrarUsuario(APIView):
    def post(self, request, *args, **kwargs):
        serializers = UserSerializer(data=request.data)

        if serializers.is_valid():
            serializers.save
            return Response(serializers.data, status=status.HTTP_201_CREATED)
    
        return Response(serializers.errors, status=status.HTTP_201_CREATED)
    