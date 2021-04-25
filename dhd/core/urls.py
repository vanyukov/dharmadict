from django.contrib import auth
from . import views

from django.urls import include, path

app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),

    path('api/v1/page/<path:url>', views.api_page_by_url, name='api_page'),
    path('api/v1/page-content/<path:url>', views.api_page_by_url_content, name='api_page'),
    path('api/v1/page/<int:page_id>', views.api_page, name='api_page'),
    path('api/v1/page/<int:page_id>/content', views.api_page_content, name='api_page_content'),

    path('api/v1/term/<str:term>', views.api_term, name='api_term'),

    path('api/v1/terms/', views.api_terms, name='api_terms'),

    # Users
    # path('profile/new', views.new_user, name='new_user'),
    # path('profile/', views.user, name='user'),
    # path('profile/change_password', views.change_user_password, name="change_user_password"),
    # path('profile/<int:user_id>', views.edit_user, name='edit_user'),
    # path('profile/<int:user_id>/delete/<operation>', views.delete_user, name="delete_user"),

    # path('profiles/paginate', views.paginate_users, name='paginate_users'),
    # path('profiles/export', views.users_export, name='export_users'),
    # path('profiles/import', views.upload_users_file, name='import_users'),
    # path('profiles/import/preview', views.upload_users_preview, name='upload_users_preview'),
    # path('profiles/import/apply', views.upload_users_apply, name='upload_users_apply'),

    path('api/v1/pages/', views.api_pages, name='api_pages'),
]