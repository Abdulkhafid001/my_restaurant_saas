from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.forms import NaijaKitchenUserCreationForm, NaijaKitchenUserChangeForm
from accounts.models import NaijaKitchenUser


class NaijaKitchenUserAdmin(UserAdmin):
    add_form = NaijaKitchenUserCreationForm
    form = NaijaKitchenUserChangeForm
    model = NaijaKitchenUser
    list_display = [
        "email",
        "username",
        "name",
        "is_staff"
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("name",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("name",)}),)


admin.site.register(NaijaKitchenUser, NaijaKitchenUserAdmin)
