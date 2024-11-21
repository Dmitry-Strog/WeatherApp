from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.user.models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('login', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('login', 'password', 'email')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('login', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('login', 'email')
    ordering = ('login',)


admin.site.register(CustomUser, CustomUserAdmin)
