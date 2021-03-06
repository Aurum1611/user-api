from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import UserProfileViewSet

router = routers.DefaultRouter()
router.register(r'users', UserProfileViewSet, basename='users')

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
