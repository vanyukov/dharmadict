import datetime
import json
import logging
import os
from email import contentmanager

from django.http import HttpResponse
from django.http.response import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.urls import include, path
from django.utils.translation import ugettext as _
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie

from .admin import CustomUserResource
from .forms import CustomUserCreationForm
from .models import (CustomUser, Term, Language, Meaning)
from .view_helpers import *
from .filters import TermFilter

# Create your views here.

def index(request):
    return HttpResponse("Буддийская терминология в русских переводах. Версия 2 – в процессе разработки.")

def delete_user(request, user_id, operation):
    if not request.user.is_authenticated or request.method != "POST" or not request.user.is_staff: return json_forbidden()
    u = get_object_or_404(CustomUser, pk=user_id)
    resp = ""
    if u.deleted:
        return json_error(message=_("Пользователь был удалён, операция недопустима"))
    if operation == "mark":
        u.mark2delete = True;
        resp = _("Пользователь помечен на удаление")
    elif operation == "unmark":
        u.mark2delete = False;
        resp = _("Пользователь восстановлён")
    elif operation == "delete":
        u.mark2delete = True;
        u.deleted = True;
        u.is_active = False;
        resp = _("Пользователь удалён")
    else:
        return json_error(message=_("Недопустимая операция"))
    u.save();
    return json_success(message=resp)

def edit_user(request, user_id):
    if not request.user.is_authenticated: return HttpResponseRedirect('/accounts/login')
    user = get_object_or_404(CustomUser, pk=user_id)
    is_self = request.user.id == user.id
    is_staff = request.user.is_staff

    if request.method == "POST":
        if not is_self and not is_staff: return HttpResponseForbidden()
        form = UserUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            fill_user_data(user, form.cleaned_data, is_staff, is_self)
            user.save()
        if is_self:
            request.session[LANGUAGE_SESSION_KEY] = user.lang.lower()
            return redirect("vr:user")
        else:
            return redirect(user)
    return render(
        request,
        'user.html',
        context=common_context(request, {
            'profile': user,
            'is_self': is_self,
        }),
    )

def new_user(request):
    if not request.user.is_authenticated or not request.user.is_staff:
        if request.method == "POST" and "validate" in request.POST: return json_forbidden()
        return HttpResponseForbidden()
    u = request.user
    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        if "validate" in request.POST:
            if form.is_valid():
                return json_success()
            else:
                return json_error(errors=form.errors.get_json_data(True))
        elif form.is_valid():
            u = form.save()
            extras = UserUpdateForm(request.POST, request.FILES)
            if extras.is_valid():
                fill_user_data(u, extras.cleaned_data, True, False)
                u.save()
            return redirect(u)
    return render(
        request,
        'user.html',
        context= common_context(request, {
            'profile': None,
            'new_user': True,
            'is_self': False,
        })
    )

def api_term(request, term):
    t = TermFilter(request.GET, Term.objects.all())
    # t = Term.objects.filter(wylie__contains=term)
    arr=[]
    for term in t.qs:
        arr.append(term.json())
    
    data=json.dumps(arr, ensure_ascii=False, indent=2)
    response = HttpResponse(data, content_type='application/json; charset=utf-8')
    return response


def api_page_by_url(request, url):
    p = Page.objects.get(url=url)
    data=json.dumps(p.json(), ensure_ascii=False, indent=2)
    response = HttpResponse(data, content_type='application/json; charset=utf-8')
    return response

def api_page_by_url_content(request, url):
    p = Page.objects.get(url=url)
    # data=json.dumps(p.json(), ensure_ascii=False, indent=2)
    response = HttpResponse(p.content)
    return response

def api_page(request, page_id):
    p = get_object_or_404(Page, pk=page_id)
    data=json.dumps(p.json(), ensure_ascii=False, indent=2)
    response = HttpResponse(data, content_type='application/json; charset=utf-8')
    return response

def api_page_content(request, page_id):
    p = get_object_or_404(Page, pk=page_id)
    response = HttpResponse(p.content)
    return response

def api_pages(request):
    result = []
    pages_qs = active_pages()
    for r in pages_qs:
        result.append(r.json_no_content())
    
    data=json.dumps(result, ensure_ascii=False, indent=2)
    response = HttpResponse(data, content_type='application/json; charset=utf-8')
    return response


def user(request):
    if not request.user.is_authenticated: return HttpResponseRedirect('/accounts/login')
    u = request.user
    if request.session[LANGUAGE_SESSION_KEY] != u.lang.lower():
        request.session[LANGUAGE_SESSION_KEY] = u.lang.lower()
        return redirect("core:user")
    return render(
        request,
        'user.html',
        context= common_context(request, {
            'profile': u,
            'is_self': True,
        } )
    )

def change_user_password(request):
    if not request.user.is_authenticated or request.method != "POST": return json_forbidden()
    u = request.user
    is_staff = u.is_staff
    form = None
    if is_staff and "user" in request.POST:
        u = get_object_or_404(CustomUser, pk=int(request.POST["user"]))

    if u.id == request.user.id:
        form = PasswordChangeForm(user=u, data=request.POST)
    elif is_staff:
        form = SetPasswordForm(user=u, data=request.POST)
    else:
        return json_forbidden()

    if form.is_valid():
        form.save()
        if request.user.id == u.id:
            update_session_auth_hash(request, form.user)
        return json_success(message=_("Пароль успешно изменён"))
    return json_error(errors=form.errors.get_json_data(True))

def users_export(request):
    response = HttpResponse(CustomUserResource().export().csv, content_type="text/csv; charset=utf-8")
    response['Content-Disposition'] = "attachment; filename=\"users_%s.csv\"" % (now_str())
    return response

def upload_users_file(request):
    if request.method == 'POST':
        form = UploadUsersCSVFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_users_csv_file(request)
            return HttpResponseRedirect(reverse('vr:upload_users_preview', args=()))
    else:
        form = UploadUsersCSVFileForm()
    return render(request, 'upload_file.html', common_context(request, {'form': form}) )


def upload_users_preview(request, apply=False):
    tmpfname = request.session['uploaded_data_filename']
    result = process_uploaded_users(tmpfname, True)
    return render(request, 'upload_preview.html' , common_context(request, {
        'import_result': result,
        'title': _('загрузка пользователей'),
        'action_link': reverse('vr:upload_users_apply')
    }))


def upload_users_apply(request, apply=False):
    tmpfname = request.session['uploaded_data_filename']
    result = process_uploaded_users(tmpfname, False)
    return HttpResponseRedirect(reverse('vr:admin', args=()))
# Paginators
def paginate_users(request):
    if not request.user.is_authenticated: return HttpResponseForbidden()
    return render(request, "paginators/users.html", context = common_context(request,
        paginator_context(request, UserFilter(request.GET, active_users()), target='users', header=True)))
