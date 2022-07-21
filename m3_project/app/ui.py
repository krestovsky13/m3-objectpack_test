from objectpack.ui import BaseEditWindow, make_combo_box
from m3_ext.ui import all_components as ext

from django.contrib.auth.models import ContentType


class CreateUpdatePermissionWindow(BaseEditWindow):

    def _init_components(self):
        super()._init_components()

        self.field__name = ext.ExtStringField(
            label='name',
            name='name',
            allow_blank=False,
            anchor='100%')

        self.field__content_type = make_combo_box(
            label='content type',
            name='content_type',
            allow_blank=False,
            anchor='100%',
            data=ContentType.objects.values_list('id', 'model'))

        self.field__codename = ext.ExtStringField(
            label='codename',
            name='codename',
            allow_blank=False,
            anchor='100%')

    def _do_layout(self):
        super()._do_layout()

        self.form.items.extend(
            (
                self.field__name,
                self.field__content_type,
                self.field__codename
            ))

    def set_params(self, params):
        super().set_params(params)

        self.height = 'auto'


class CreateUpdateUserWindow(BaseEditWindow):

    def _init_components(self):
        super()._init_components()

        self.field__password = ext.ExtStringField(
            label='password',
            name='password',
            allow_blank=False,
            anchor='100%')

        self.field__last_login = ext.ExtDateField(
            label='last login',
            name='last_login',
            anchor='100%')

        self.field__superuser_status = ext.ExtCheckBox(
            label='superuser status',
            name='superuser_status',
            anchor='100%')

        self.field__username = ext.ExtStringField(
            label='username',
            name='username',
            allow_blank=False,
            anchor='100%')

        self.field__first_name = ext.ExtStringField(
            label='first name',
            name='first_name',
            anchor='100%')

        self.field__last_name = ext.ExtStringField(
            label='last name',
            name='last_name',
            anchor='100%')

        self.field__email_address = ext.ExtStringField(
            label='email address',
            name='email_address',
            anchor='100%')

        self.field__staff_status = ext.ExtCheckBox(
            label='staff status',
            name='staff_status',
            anchor='100%')

        self.field__active = ext.ExtCheckBox(
            label='active',
            name='active',
            anchor='100%',
            checked=True)

        self.field__date_joined = ext.ExtDateField(
            label='date joined',
            name='date joined',
            anchor='100%')

    def _do_layout(self):
        super()._do_layout()

        self.form.items.extend(
            (
                self.field__password,
                self.field__last_login,
                self.field__superuser_status,
                self.field__username,
                self.field__first_name,
                self.field__last_name,
                self.field__email_address,
                self.field__staff_status,
                self.field__active,
                self.field__date_joined
            ))

    def set_params(self, params):
        super().set_params(params)

        # self.title = 'User: Добавление'
        self.height = 'auto'
