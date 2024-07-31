from typing import List
from django.db.transaction import atomic
from django.contrib.auth.models import Group

from ..selectors.permission_selectors import permission_exist
from ..selectors.group_selectors import get_group_by_id, permissions_already_in_group

@atomic(using='default')
def create_group(*, group_data : dict) -> Group:
    # get permissions
    if not permission_exist(permission_ids=group_data.get("permissions")):
        raise ValueError(f'not found permissions {group_data["permissions"]}')
    
    # create group
    group = Group.objects.create(name=group_data.get("name"))
    # add permissions
    group.permissions.add(*group_data.get("permissions"))
    return group

@atomic(using='default')
def add_permissions_to_group(*, group_id : int, permission_ids : List[int]) -> Group:
    
    if not permission_exist(permission_ids=permission_ids):
        raise ValueError(f'not found permissions {permission_ids}')
    
    if permissions_already_in_group(permission_ids=permission_ids):
        raise ValueError(f'permissions {permission_ids} already in group')
    
    group = get_group_by_id(id=group_id)
    group.permissions.add(*permission_ids)
    return group