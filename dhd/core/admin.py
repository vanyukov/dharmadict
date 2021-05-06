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
            'user_permissions', 
            'img', 
            'password',
            'isTranslator',
            'page', 
            'deleted'
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

#--------
class CustomUserAdmin(UserAdmin, ImportExportModelAdmin):
    resource_class = CustomUserResource
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'last_name', 'first_name', 'middle', 'email', 'isTranslator', 'page', 'img']
    # Add fields to admin page
    fieldsets = UserAdmin.fieldsets
    fieldsets[1][1]["fields"] = ('last_name', 'first_name', 'middle', 'email', 'isTranslator', 'page', 'img')
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('last_name', 'first_name', 'middle',)}),
    )

class PageAdmin(ImportExportModelAdmin):
    resource_class = PageResource
    list_display = ['url', 'title', 'shortTitle', 'keywords', 'description', 'created', 'modified', 'published', 'mainMenuLink', 'mainPageLink']


class LanguageAdmin(ImportExportModelAdmin):
    resource_class = LanguageResource
    list_display = ['code', 'name',]

class TermAdmin(ImportExportModelAdmin):
    resource_class = TermResource
    list_display = ['wylie', 'sa2ru1', 'sa2ru2', 'sa2ru3', 'sa2en1', 'sa2en2', 'sa2en3', 'sanscrit', 'tibetan']

class MeaningAdmin(ImportExportModelAdmin):
    resource_class = MeaningResource
    list_display = ['meaning', 'term', 'translator', 'language', 'comment', 'interpretation', 'context', 'rationale']



# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Term, TermAdmin)
admin.site.register(Meaning, MeaningAdmin)
