"""
classe responsável por converter os objetos do django, como modelos django, em dados primitivos como dicionários, que podem ser facilmente adicionados em arquivos JSON ou no banco de dados, e vice-versa.
"""

from rest_framework.serializers import ModelSerializer
from .models import UserProfile

class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'