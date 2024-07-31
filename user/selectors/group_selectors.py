from typing import List

from django.contrib.auth.models import Group

def get_all_groups():
    return Group.objects.all()

def get_group_by_id(*, id : int):
    return Group.objects.get(id=id)

def permissions_already_in_group(*, permission_ids : List[int]):
    return Group.objects.filter(permissions__in=permission_ids).exists()