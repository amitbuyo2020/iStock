from django.contrib import admin
from .models import CustomUser, Profile
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ('email', 'is_active', 'is_superuser', 'is_staff')
    list_filter = ()
    fieldsets = (
        (None, {
            'fields': ('email', 'password')
        }),
        ('Permissions', {
            'fields': ('is_staff', 'is_active')
        })
    )

    add_fieldsets = (
        (
            None, {
                'classes': 'wide',
                'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')
            }
        ),
    )

    search_fields = ('email', )
    ordering = ('email', )

class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ('username', 'bio', 'address', 'user')
    list_filter = ()
    fieldsets = (
        ('General Information', {
            'fields': ('username', 'bio', 'user')
        }),
        ('Residence' , {
            'fields': ('address', )
        })
    )
    add_fieldsets = (
        (
            'Update profile', {
                'classes': 'wide',
                'fields': ('username', 'bio', 'address')
            }
        ),
    )
    search_fields = ('username', )
    ordering = ('username', )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)