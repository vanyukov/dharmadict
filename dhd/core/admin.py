from django.contrib import admin

from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import (CustomUser, Page, Language, Term, Meaning)

from import_export import resources
from import_export.admin import ImportExportModelAdmin

class CustomUserResource(resources.ModelResource):
    class Meta:
        model = CustomUser
        export_order = (
            'id', 
            'username',
            'last_name', 
            'first_name',
            'middle',
            'email',
            'is_active',
            'is_superuser', 
            'is_staff', 
            'last_login',
            'date_joined',
            'groups',
            'user_permissions', 'img', 'password', 'deleted'
        )


class PageResource(resources.ModelResource):
    class Meta:
        model = Page

class LanguageResource(resources.ModelResource):
    class Meta:
        model = Language

class TermResource(resources.ModelResource):
    class Meta:
        model = Term

class MeaningResource(resources.ModelResource):
    class Meta:
        model = Meaning


class CustomUserAdmin(UserAdmin, ImportExportModelAdmin):
    resource_class = CustomUserResource
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'first_name', 'email', 'img']
    # Add fields to admin page
    fieldsets = UserAdmin.fieldsets
    fieldsets[1][1]["fields"] = ('last_name', 'first_name', 'middle', 'email', 'img')
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('last_name', 'first_name', 'middle',)}),
    )


# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Page)
admin.site.register(Language)
admin.site.register(Term)
admin.site.register(Meaning)
