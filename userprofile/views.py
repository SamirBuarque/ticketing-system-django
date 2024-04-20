from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from models import UserProfile
from serializers import UserProfileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class UserProfileViewset(APIView):
    def get(self, request, id=None):
        if id:
            # item = objeto com id único gerado automaticamente pelo framework
            item = UserProfile.objects.get(id=id)
            serializer = UserProfileSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = UserProfile.objects.all()
        serializer = UserProfileSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() # inserindo na tabela
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        item = UserProfile.objects.get(id=id)
        serializer = UserProfileSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        item = UserProfile.objects.filter(id=id)
        print(item)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})