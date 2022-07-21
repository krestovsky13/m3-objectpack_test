import objectpack
from django.contrib.auth.models import User, Group, Permission, ContentType
from objectpack.actions import ObjectPack

from . import ui


class ContentTypePack(ObjectPack):
    model = ContentType

    add_to_desktop = True
    add_window = edit_window = objectpack.ui.ModelEditWindow.fabricate(model)


class UserPack(ObjectPack):
    model = User

    add_to_desktop = True
    add_window = edit_window = ui.CreateUpdateUserWindow


class GroupPack(ObjectPack):
    model = Group

    add_to_desktop = True
    add_window = edit_window = objectpack.ui.ModelEditWindow.fabricate(model)


class PermissionPack(ObjectPack):
    model = Permission

    add_to_desktop = True
    parent_field = 'content_type'

    add_window = edit_window = ui.CreateUpdatePermissionWindow

    def save_row(self, obj, create_new, request, context, *args, **kwargs):
        content_type_id = getattr(context, self.parent_field, None)
        setattr(obj, '%s_id' % self.parent_field, content_type_id)
        obj.save()
