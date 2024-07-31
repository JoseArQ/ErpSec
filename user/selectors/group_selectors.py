from django.contrib.auth.models import Group

def get_all_groups():
    return Group.objects.all()