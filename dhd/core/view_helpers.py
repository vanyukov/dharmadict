from json import dumps

from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseForbidden
from django.utils.translation import LANGUAGE_SESSION_KEY
from django.core.paginator import Paginator

from core.models import (CustomUser, Page)
from django.conf import settings

def json_forbidden(message=None):
    if message == None:
        message = _("Доступ запрещён")
    return HttpResponse(dumps({"success": False, "message": message}), content_type="application/json", status=403)


def json_success(message="", data=None):
    return HttpResponse(dumps({"success": True, "data": data, "message": message}, ensure_ascii=False, indent=2), content_type="application/json", status=200 )


def json_error(errors=None, message=""):
    return HttpResponse(dumps({"success": False, "errors": errors, "message": message}), content_type="application/json", status=400)


def forbidden(request: HttpRequest):
    if "application/json" in request.META["HTTP_ACCEPT"]:
        return json_forbidden()
    return HttpResponseForbidden()

def common_context(request: HttpRequest, *args):
    ctx = {
        'user': request.user,
        'is_staff': request.user.is_staff,
        # 'org': settings.ORG_NAME
    }
    if request.resolver_match != None:
        ctx['view'] = request.resolver_match.view_name
    for subctx in args:
        if subctx != None:
            ctx.update(subctx)
    return ctx

def simple_paginator(request, filter, key, filter_key=None, path=None):
    if filter_key == None:
        filter_key = key+"_filter"
    return paginator_context(request, filter, key, filter_key, header=True, data_only=False, path=path)

def paginator_context(request, filter, key = 'entries', filter_key='filter', header=False, data_only=True, target=None, per_page=10, fullwidth=False, path=None, default_order="-id", alldata=False):

    if path == None and request.resolver_match:
        path = request.resolver_match.view_name

    qs = filter.qs

    order = default_order
    if 'order_by' in request.GET:
        order = request.GET['order_by']
    else:
        qs = qs.order_by(order)

    page = 1
    if 'page' in request.GET:
        page = request.GET['page']
    if 'show_header' in request.GET:
        header = True

    return {
        'data_only': data_only,
        'target': target if target != None else key,
        'disable_header': not header,
        'order': order,
        'fullwidth': fullwidth,
        'path': path,
        filter_key: filter.form,
        key: qs if alldata else Paginator(qs, per_page).get_page(page),
        'extended': "extended" in request.GET or 'extra_fields' in request.GET,
        'extra_fields': "extra_fields" in request.GET,
    }
    # ctx[key] =
        # 'entries': patients.get_page(page),
        # 'data_only': True,
        # 'target': "patients",
        # 'disable_header': True,
        # 'order': request.GET["order_by"],
        # 'path': "vr:paginate_patients",
        # 'filter': filters.form

def stats_context(request, extra=None, patient=None):
    if patient != None:
        return common_context(request, extra, {
            'total_results': active_results().filter(patient=patient).count(),
            'total_exercies': active_result_entries().filter(is_measurement=False, result__patient=patient).count(),
            'total_measurements': active_result_entries().filter(is_measurement=True, result__patient=patient).count(),
        })
    return common_context(request, extra, {
        'total_patients': active_patients().count(),
        'total_results': active_results().all().count(),
        'total_exercies': active_result_entries().filter(is_measurement=False).count(),
        'total_measurements': active_result_entries().filter(is_measurement=True).count(),
    })

def active_users():
    return CustomUser.active_users()

def active_pages():
    return Page.objects.filter(deleted=False, published=True)

# def patient_statistics(pk, is_measurement = None):
#     qs = active_result_entries().select_related('result', 'result__user', 'result__patient').filter(result__patient__pk=pk)
#     if is_measurement != None:
#         return qs.filter(is_measurement=is_measurement)
#     return qs

def fill_user_data(user, data, is_staff, is_self):
    if data["lang"]:
        user.lang = data["lang"]
    if data["img"]:
        user.img = data["img"]
    user.phone = data["phone"]
    user.note = data["note"]
    if is_staff:
        if not is_self:
            if data["status"]:
                user.is_active = data["status"] == "Active"
            if data["role"]:
                user.is_staff = data["role"] == "admin"
            # I'm not responsible for potential dangers this might incur
            if data["username"]:
                user.username = data["username"]
            if data["email"]:
                user.email = data["email"]
        if data["name"]:
            user.first_name = data["name"]
        if data["surname"]:
            user.last_name = data["surname"]
        if data["middlename"]:
            user.middle = data["middlename"]


class ModelLocaleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request: HttpRequest):
        response = self.get_response(request)
        if hasattr(request, 'session') and hasattr(request, 'user') and request.user.is_authenticated:
            request.session[LANGUAGE_SESSION_KEY] = request.user.lang.lower()
        return response

