from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .forms import CreationUserForm, ChangeForm

Users = get_user_model()

class MyUserAdmin(UserAdmin):
    add_form=CreationUserForm
    readonly_fields=('date_joined',)
    form=ChangeForm
    model=Users
    search_fields = ('email',)
    list_filter=['is_admin', 'is_staff']
    list_display=['username', 'email', 'first_name', 'last_name', 'date_birthday', 'usernumber', 'date_joined', ]
    ordering = ('username',)

    fieldsets = (
        (None, {'fields': ('email',)}),
        ('Permissions', {'fields': ('is_admin','is_staff')}),
        ('Primary personal information', {
            'fields': ('first_name', 'last_name',  'date_birthday', 'usernumber', 'date_joined',)}),
        ('Status', {'fields': ('is_active', )}),
    )

admin.site.register(Users, MyUserAdmin)

# Register your models here.
