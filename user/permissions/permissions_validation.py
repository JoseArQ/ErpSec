from django.core.exceptions import PermissionDenied

from ..models import User

def validate_user_permission(user : User, module_name : str, action : str) -> None:
    
    permission_codename = f"{module_name}.{action}_{module_name}"
    
    if not user.has_perm(permission_codename):
        raise PermissionDenied(f"You do not have permission to {action} in module {module_name}.")