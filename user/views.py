from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated

from .serializers.user_serializers import UserSerializer
from .serializers.permission_serializer import PermissionSerializer

from .services.user_services import create_user, add_permissions_to_user
from .selectors.user_selectors import get_all_users
from .selectors.permission_selectors import get_all_permissions

class UserViewSet(GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        user = request.user

        new_user_data = request.data.copy()
        new_user_serializer = self.get_serializer(data=new_user_data)

        if not new_user_serializer.is_valid():
            return Response(
                data={"errors": new_user_serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )
        new_user = create_user(user_data=new_user_data)
        
        return Response(
             data={
                "user": self.get_serializer(new_user).data,
             }, 
            status=status.HTTP_200_OK
        )
    
    def list(self, request, *args, **kwargs):
        
        return Response(
            data={
                "users": self.get_serializer(
                    get_all_users(),
                    many=True,
                    ).data,
            },
            status=status.HTTP_200_OK
        )

    @action(methods=["PATCH"], detail=True)
    def add_permissions(self, request, pk=None, *args, **kwargs):
        body = request.data.copy()
        
        permission_ids = body.get("permission_ids", None)
        
        if not permission_ids:
            return Response(
                data={"error": "permission_ids field is required."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        add_permissions_to_user(user_id=pk, permission_ids=permission_ids)
        return Response(
            data={"message": "permissions added successfully!"},
            status=status.HTTP_200_OK,
        )
    
class PermissionViewSet(GenericViewSet):
    serializer_class = PermissionSerializer
    
    def list(self, request, *args, **kwargs):
        
        permissions_serializer = self.get_serializer(get_all_permissions(), many=True)
    
        return Response(
            data={
                "permissions": permissions_serializer.data
            }, 
            status=status.HTTP_200_OK
            )
    