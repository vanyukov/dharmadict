import math
from datetime import timedelta

from django.template.defaultfilters import date as ddate
from django.template.defaultfilters import floatformat
from django.template.library import Library
from django.utils.safestring import mark_safe
from django.utils.translation import gettext as _


register = Library()

@register.filter(is_safe=True)
def select(value, expect):
    sel_name = "selected"
    if ";check" in expect:
        expect = expect[:-6]
        sel_name = "checked"
    if ';def' in expect:
        expect = expect[:-4]
        if value == None:
            return mark_safe("%s value=\"%s\"" % (sel_name, expect[:-4]))
    if value == expect:
        return mark_safe("%s value=\"%s\"" % (sel_name, expect))
    return mark_safe("value=\"%s\"" % expect)

@register.simple_tag(takes_context=True)
def navcheck(context, expect, vtrue, vfalse):
    if "view" in context and context["view"] == expect:
        return vtrue
    return vfalse

@register.simple_tag(takes_context=True)
def nvacheckbtn(context, expect):
    return navcheck(context, expect, "btn btn-secondary", "btn btn-primary")

@register.filter(expects_localtime=True, is_safe=False)
def udate(value):
    return ddate(value, 'd M Y H:i')

@register.simple_tag(takes_context=True)
def patient_header(context):
    if "patient" in context and context["patient"] != None: return " - " + str(context['patient'])
    return ""

@register.simple_tag
def exercise_options(is_exercise):
    ret = ["<option selected value=''>" + _("Любое") + "</option>"]
    mask = TYPE_EXERISE if is_exercise else TYPE_MEASUREMENT
    for e in get_exercise_list():
        if (e[2] & mask) == mask:
            ret.append("<option value='" + e[0] + "'>" + str(e[1]) + "</option>")
    return mark_safe("\n".join(ret))

@register.simple_tag(takes_context=True)
def even_odd(context, tag="auto", flip=True):
    tag = "__evenodd_" + tag
    if tag not in context:
        context[tag] = False
    elif flip:
        context[tag] = not context[tag]
    return "d-even" if context[tag] else "d-odd"

@register.filter
def reltime(v):
    v = float(v)
    sec = math.floor(v % 60)
    mins = math.floor(v / 60)
    return "%02d:%02d" % (mins, sec)

@register.filter
def infout(v):
    v = float(v)
    if math.isinf(v) or math.isnan(v):
        return "-"
    return floatformat(v, "2")

@register.simple_tag
def iteration_counter(it):
    return  _("%d из %d") %(it.performed, it.designated)
@register.simple_tag
def x_out_of_y(a, b):
    return _("%d из %d") %(a, b)

def get_rowc(context):
    return (context[context["target"] + "_rowc"], context[context["target"] + "_rown"])

# A bit hacky, but given that it was done at later stage with sudden spec change: It shall be hacky and I'm not sorry for it
@register.simple_tag(takes_context=True)
def calc_row_counts(context, records):
    vmax = 1;
    vnames = []
    tagFilter = None
    if "filter" in context:
        tagFilter = context["filter"]["parese"].data
    vtypes = context["value_types"]
    for rec in records:
        val = math.ceil((rec.values.count()+1) / 2)
        if val > vmax:
            vmax = val
        for v in rec.values.all():
            if v.display_name not in vnames:
                if tagFilter is not None:
                    found = False
                    for t in vtypes:
                        if t[0] == v.display_name and tagFilter not in t[2]:
                            found = True
                            break
                    if found:
                        continue
                vnames.append(v.display_name)

    vnames.sort()
    vnames.insert(vmax, "_hold")
    vmax = math.ceil((len(vnames) + 1) / 2)
    context[context["target"] + "_rowc"] = vmax
    context[context["target"] + "_rown"] = vnames
    return ""

@register.simple_tag(takes_context=True)
def calc_val_header(context, rid):
    (rowc, rown) = get_rowc(context)
    start = rowc * rid
    vmax = min(len(rown), start+rowc)
    colmax = start + rowc
    result = ""

    while start < colmax:
        if start >= vmax:
            result += "<th colspan='3'></th>"
        elif rown[start] == "_hold":
            result += "<th colspan='3'>%s<br>%s</th>" % ( _(rown[start]), _("мин/сред/макс") )
        else:
            result += "<th colspan='3'>%s</th>" % ( _(rown[start]), )
        start += 1
    return mark_safe(result)

@register.simple_tag(takes_context=True)
def calc_val_row(context, record, rid):
    (rowc, rown) = get_rowc(context)
    start = rowc * rid
    vmax = min(len(rown), start + rowc)
    colmax = start + rowc
    result = []
    vals = record.values.all()
    while start < colmax:
        if start >= vmax:
            result.append("<td colspan='3' class='text-center border-right'>-</td>")
        elif rown[start] == "_hold":
            result.append(calc_val(record.hold_min, record.hold_avg, record.hold_max))
        else:
            name = rown[start]
            found = False
            for val in vals:
                if val.display_name == name:
                    result.append(calc_val(val.vmin, val.vavg, val.vmax))
                    found = True
                    break
            if not found:
                result.append("<td colspan='3' class='text-center border-right'>-</td>")
        start += 1
    return mark_safe(''.join(result))

@register.simple_tag
def calc_val(vmin, vavg, vmax):
    return "<td class='slim br border-left'>%s</td><td class='slim br'>%s</td><td class='slim border-right'>%s</td>" % (infout(vmin),infout(vavg),infout(vmax))

@register.filter
def enum_active_mode(value):
    return ACITVE_MODE[value]
