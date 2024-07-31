from typing import List
from django.db.transaction import atomic
from django.contrib.auth.models import Group

from ..selectors.permission_selectors import permission_exist

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