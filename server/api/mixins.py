from rest_framework import permissions

from .permissions import IsStaffEditorPermissions

class staffEditorPermissionMixin():
  permission_classes = [permissions.IsAdminUser, IsStaffEditorPermissions]

class UserQuerySetMixin():
  """
  Filter content by it's user/owner Mixin
  """
  user_field = 'user'

  def get_queryset(self, *args, **kwargs):
    lookup_data = { self.user_field : self.request.user }
    qs = super().get_queryset(*args, **kwargs)
    return qs if self.request.user.is_staff else qs.filter(**lookup_data)
