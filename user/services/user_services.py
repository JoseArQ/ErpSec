from typing import Dict, Any, List
from django.db.transaction import atomic

from ..models import User
from ..selectors.user_selectors import get_user_by_id
from ..selectors.permission_selectors import permission_exist

def create_user(*, user_data : Dict[str, Any]) -> User:
    return User.objects.create_user(**user_data)

@atomic(using='default')
def add_permissions_to_user(*, user_id : int, permission_ids : List[int]):
    user = get_user_by_id(id=user_id)

    if not permission_exist(permission_ids=permission_ids):
        raise ValueError(f'not found permissions {permission_ids}')
    
    user.user_permissions.add(**permission_ids)
