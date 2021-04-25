from django.contrib.postgres.search import SearchQuery
from django.db.models import Q
from django.db.models.query import QuerySet
from django.forms.fields import TypedMultipleChoiceField
from django_filters.filters import CharFilter, ChoiceFilter, OrderingFilter
from django_filters.filterset import FilterSet

from .models import (Term, Meaning)

class TermFilter(FilterSet):
    order_by = OrderingFilter(
        fields = (
            ('id', 'id'),
            ('wylie', 'wylie'),
            ('sa2ru', 'sa2ru'),
            ('sa2en', 'sa2en'),
            ('tibetan', 'tibetan'),
            ('sanscrit', 'sanscrit'),
        )
    )

    full_term = CharFilter('full_term', method='full_term_filter')

    def full_term_filter(self, queryset:QuerySet, name, value):
        if value == "":
            return queryset
        vals = value.split(" ")
        value = vals.pop()
        qval = Q(wylie__istartswith=value) | Q(sa2ru__istartswith=value) | Q(sa2en__istartswith=value) | Q(tibetan__istartswith=value) | Q(sanscrit__istartswith=value)
        for val in vals:
            qval = qval | Q(wylie__istartswith=value) | Q(sa2ru__istartswith=value) | Q(sa2en__istartswith=value) | Q(tibetan__istartswith=value) | Q(sanscrit__istartswith=value)
        return queryset.filter(qval)

    class Meta:
        model = Term
        fields = {
            "wylie": ["icontains"],
            "sa2ru": ["icontains"],
            "sa2en": ["icontains"],
            "tibetan": ["icontains"],
            "sanscrit": ["icontains"],
        }

