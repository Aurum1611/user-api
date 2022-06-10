from rest_framework import viewsets
from .models import UserProfile
from .serializers import UserProfileSerializer
from django.db.models import Q, F
from rest_framework.filters import SearchFilter
from rest_framework.response import Response


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('is_active',)
    
    def get_queryset(self):
        mail = self.request.query_params.get('email')
        if mail:
            users = [UserProfile.objects.get(email=mail),]
        else:
            users = UserProfile.objects.all()
        return users
    
    def partial_update(self, request, *args, **kwargs):
        user = self.get_object()
        user.city = request.data.get('city', user.city)
        user.save()

        serializer = UserProfileSerializer(user)
        return Response(serializer.data)
