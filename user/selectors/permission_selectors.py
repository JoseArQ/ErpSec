from typing import List
from django.db.models import QuerySet
from django.contrib.auth.models import Permission

def permission_exist(*, permission_ids : List[int]) -> bool:
    return Permission.objects.filter(id__in=permission_ids).exists()

def get_all_permissions() -> QuerySet[Permission]:
   return Permission.objects.all()