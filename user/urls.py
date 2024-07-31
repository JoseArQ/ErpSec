from django.urls import path, include

from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, PermissionViewSet, GroupViewSet

user_router = DefaultRouter()
user_router.register(prefix=r'users', viewset=UserViewSet, basename='user')

permission_router = DefaultRouter()
permission_router.register(prefix=r'permissions', viewset=PermissionViewSet, basename='permission')

group_router = DefaultRouter()
group_router.register(prefix=r'groups', viewset=GroupViewSet, basename='groups')

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(user_router.urls)),
    path('', include(permission_router.urls)),
    path('', include(group_router.urls)),

]