from rest_framework import permissions

from .permissions import IsStaffEditorPermissions

class staffEditorPermissionMixin():
  permission_classes = [permissions.IsAdminUser, IsStaffEditorPermissions]
