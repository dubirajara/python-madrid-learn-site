from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserLearn


class CustomUserAdmin(UserAdmin):
    fieldsets = ()
    add_fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )

    list_display = ('username', 'email', 'is_active', 'is_staff',)
    search_fields = ('username',)
    ordering = ('username',)


admin.site.register(UserLearn, CustomUserAdmin)
